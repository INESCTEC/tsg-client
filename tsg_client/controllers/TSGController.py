import os
import json
import requests
import bcrypt
import urllib.parse

from datetime import datetime
from loguru import logger

from tsg_client.controllers.RequestController import RequestController
from tsg_client.controllers.Endpoints import Endpoints
from tsg_client.controllers.SelfDescription import SelfDescription
from tsg_client.utils.file_handling import save_pdf_file, save_csv_file, save_json_file


def is_contract_valid(contract_offer_dict):
    today = datetime.utcnow()
    try:
        start_date = datetime.strptime(
            contract_offer_dict["ids:contractStart"]["@value"], "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        end_date = datetime.strptime(
            contract_offer_dict["ids:contractEnd"]["@value"], "%Y-%m-%dT%H:%M:%S.%fZ"
        )
    except ValueError:
        # Handle invalid date format gracefully
        print(
            "Invalid date format in contract offer. Please check the format and try again."
        )
        return False

    return start_date <= today <= end_date


class TSGController:
    def __init__(
        self, api_key, connector_id, access_url, agent_id=None, metadata_broker_url=None
    ):
        self.catalogs = None
        self.api_key = api_key
        self.connector_id = connector_id
        self.access_url = access_url
        self.agent_id = agent_id
        self.metadata_broker_url = metadata_broker_url

        # Start core container (connector) http requests controller:
        self.endpoints = Endpoints()
        self.controller = RequestController(
            base_url=self.access_url,
            connector_id=self.connector_id,
            agent_id=self.agent_id,
            api_key=self.api_key,
        )

        self.__validate_connection()

    def __repr__(self):
        return (
            f"TSGController(connector_id={self.connector_id}, "
            f"access_url={self.access_url}, "
            f"agent_id={self.agent_id})"
        )

    def __validate_connection(self):
        # Check if the inter-connector API is available and reachable with
        # this API_KEY and ACCESS_URL.
        try:
            self.controller.get(
                endpoint=self.endpoints.RESOURCES, expected_status_code=200
            )
        except Exception as e:
            raise Exception(f"Error connecting to the TSG connector: {repr(e)}")

    def get_connector_selfdescription(self,
                                      access_url,
                                      agent_id="",
                                      connector_id=""):
        """
        Get self-descriptions from a connector from another dataspace
        participant, given its connector CONNECTOR_ID and ACCESS_URL.

        :param access_url: Access URL
        :type access_url: str
        :param connector_id: (optional) Connector ID
        :type connector_id: str
        :param agent_id: (optional)  Agent ID
        :type agent_id: str
        :return: SelfDescription object
        """

        _access_url = f"{access_url}/selfdescription"

        params = {
            "connectorId": connector_id,
            "accessUrl": _access_url,
            "agentId": agent_id,
        }
        rsp = self.controller.get(
            endpoint=self.endpoints.DESCRIPTION, params=params, expected_status_code=200
        )
        try:
            selfdescription = SelfDescription.from_dict(rsp.json())
        except ValueError as ve:
            selfdescription = "error"
            logger.exception(f"Error creating SelfDescription: {ve}")

        return selfdescription

    @staticmethod
    def parse_resource_catalogs(self_description):
        return self_description.catalogs

    @staticmethod
    def parse_catalog_artifacts(
        self_description,
        catalog_id=None,
        resource_type: str = None,
        creation_date_gt: str = None,
        creation_date_lt: str = None,
        return_last_artifact: bool = False,
        valid_contract_only: bool = False,
    ):
        """
        Parse the artifacts from a connector's self-description catalog.

        :param self_description: SelfDescription object
        :type self_description: SelfDescription
        :param catalog_id: Catalog ID to filter the artifacts
        :type catalog_id: str
        :param resource_type: Resource type to filter the artifacts
        :type resource_type: str
        :param creation_date_gt: Filter artifacts created after this date
        :type creation_date_gt: str
        :param creation_date_lt: Filter artifacts created before this date
        :type creation_date_lt: str
        :param return_last_artifact:  Return only the last artifact
        :type return_last_artifact: bool
        :param valid_contract_only: Return only valid contracts
        :type valid_contract_only: bool
        :return: Valid artifacts list
        """
        artifacts = []

        if self_description.catalogs:
            for catalog in self_description.catalogs:
                if catalog_id and catalog.id != catalog_id:
                    continue
                for resource in catalog.offeredResource:
                    if resource.contract_offer == "":
                        logger.warning(
                            f"Resource {resource.artifact_id} "
                            f"has no registered "
                            f"contract offer and "
                            f"will be ignored."
                        )
                        continue
                    contract_offer_str = resource.contract_offer
                    contract_offer_str_fixed = contract_offer_str.replace("'", '"')
                    contract_offer_dict = json.loads(contract_offer_str_fixed)
                    if resource_type and contract_offer_dict["@type"] != resource_type:
                        continue
                    creation_date = datetime.strptime(
                        resource.created, "%Y-%m-%dT%H:%M:%S.%fZ"
                    )
                    if creation_date_gt and creation_date <= datetime.strptime(
                        creation_date_gt, "%Y-%m-%dT%H:%M:%S.%fZ"
                    ):
                        continue
                    if creation_date_lt and creation_date >= datetime.strptime(
                        creation_date_lt, "%Y-%m-%dT%H:%M:%S.%fZ"
                    ):
                        continue
                    if return_last_artifact and resource != catalog.offeredResource[-1]:
                        continue
                    if valid_contract_only and not is_contract_valid(
                        contract_offer_dict
                    ):
                        continue
                    artifacts.append(
                        {
                            "id": resource.artifact_id,
                            "contract_offer": resource.contract_offer,
                            "artifact_created": resource.created,
                            "access_url": resource.access_url,
                            "title": resource.title,
                            "description": resource.description,
                        }
                    )
        return artifacts

    def request_agreement(
        self, connector_id, artifact_access_url, artifact_contract_offer
    ):
        """
        Request Contract Agreement for a data artifact from another connector,

        :param connector_id: Connector ID
        :type connector_id: str
        :param artifact_access_url: Artifact access URL
        :type artifact_access_url: str
        :param artifact_contract_offer: Artifact contract offer
        :type artifact_contract_offer: str
        :return: Contract Agreement ID
        """
        payload = {
            "connectorId": connector_id,
            "agentId": "",
            "contractOffer": artifact_contract_offer,
            "accessUrl": artifact_access_url,
        }

        rsp = self.controller.post(
            endpoint=self.endpoints.CONTRACT_REQUEST, data=payload, files={"a": "a"}
        )

        return rsp.json()["@id"]

    def request_data_artifact(
        self,
        artifact_id,
        artifact_access_url,
        connector_id,
        agent_id,
        contract_agreement_id,
        keep_original_format,
        file_path,
    ):
        """
        Request a data artifact from another connector, given the artifact
         ACCESS_URL.

        :param artifact_id: Artifact ID
        :type artifact_id: str
        :param artifact_access_url: Artifact access URL
        :type artifact_access_url: str
        :param connector_id: Connector ID
        :type connector_id: str
        :param agent_id: Agent ID
        :type agent_id: str
        :param contract_agreement_id: Contract agreement ID
        :type contract_agreement_id: str
        :param keep_original_format: Keep original format of the artifact (e.g., PDF, CSV, etc.)
        :type keep_original_format: bool
        :param file_path: Path to save the artifact file
        :type file_path: str
        """

        params = {
            "artifact": artifact_id,
            "connectorId": connector_id,
            "agentId": agent_id,
            "accessUrl": artifact_access_url,
            "transferContract": contract_agreement_id,
        }
        rsp = self.controller.get(
            endpoint=self.endpoints.ARTIFACTS_CONSUMER, params=params
        )

        # Remove spaces & special characters from artifact_id
        artifact_id = artifact_id.strip().replace(":", "_")

        if not keep_original_format:
            txt_filename = f"{artifact_id}.txt"
            txt_path = os.path.join(os.getcwd(), txt_filename)
            with open(txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(rsp.text)
            return {"message": f"Text file saved to {txt_path}"}

        content_type = rsp.headers.get("content-type")
        if content_type == "application/json":
            return save_json_file(artifact_id, rsp.text, file_path)
        elif content_type == "application/pdf":
            return save_pdf_file(artifact_id, rsp.content, file_path)
        elif content_type == "text/csv":
            return save_csv_file(artifact_id, rsp.text, file_path)
        else:
            return {"message": "Unsupported format"}

    def publish_data_artifact(self, artifact_file, title, description, contract_offer, catalog_id=None):
        """
        Publish a data artifact for this connector

        :param title: Artifact title
        :type title: str
        :param artifact_file: Multipart file containing the artifact
        :type artifact_file: file-like object
        :param description: Artifact description
        :type description: str
        :param contract_offer: Contract offer
        :type contract_offer: str
        :param catalog_id: Catalog ID (optional)
        :type catalog_id: str
        """

        ids_permission = [
            permission["@id"] for permission in json.loads(contract_offer).get('ids:permission', [])
        ]

        if ids_permission:
            rsp = self.controller.get(endpoint=self.endpoints.OFFERS)
            rsp_json = rsp.json()

            used_ids_permission = [
                permission["@id"]
                for obj in rsp_json
                for permission in obj.get("ids:permission", [])
            ]

            ids_permission_set = set(ids_permission)
            used_ids_permission_set = set(used_ids_permission)

            common_permissions = ids_permission_set & used_ids_permission_set

            if common_permissions:
                raise ValueError("It is not allowed to reuse ids:Permission @id on contracts.")
        
        payload = {
            "title": title,
            "description": description,
            "contractOffer": contract_offer,
        }

        files = {
            'artifact': artifact_file
        }

        endpoint = self.endpoints.ARTIFACTS_PROVIDER

        rsp = self.controller.post(
            endpoint=endpoint, data=payload, files=files
        )
        rsp_json = rsp.json()

        if catalog_id:
            endpoint = f'api/resources/{catalog_id}'

            headers = {
                'Content-type': 'application/json',
            }

            self.controller.post(
                endpoint=endpoint, data=rsp_json, headers=headers
            )

        return rsp_json


    def delete_artifact(self, artifact_id):
        """
        Delete an artifact from this connector
        """

        encoded_string = urllib.parse.quote(artifact_id, safe="")
        endpoint = self.endpoints.ARTIFACTS_PROVIDER + "/" + encoded_string

        self.controller.delete(endpoint=endpoint, expected_status_code=200)

    def edit_artifact(self, artifact_id, artifact, title, description, contract_offer):
        """
        Edit an artifact from this connector

        :param artifact_id: Artifact ID
        :type artifact_id: str
        :param artifact: Artifact object
        :type artifact: str
        :param title: Artifact title
        :type title: str
        :param description: Artifact description
        :type description: str
        :param contract_offer: Contract offer

        """
        payload = {
            "artifact": artifact,
            "title": title,
            "description": description,
            "contractOffer": contract_offer,
        }

        encoded_string = urllib.parse.quote(artifact_id, safe="")
        endpoint = self.endpoints.ARTIFACTS_PROVIDER + "/" + encoded_string

        rsp = self.controller.put(endpoint=endpoint, data=payload, files=payload)
        return rsp.json()

    def get_connector_self_selfdescription(self):
        """
        Get self-description from this connector

        :return: SelfDescription object
        """

        rsp = self.controller.get(
            endpoint=self.endpoints.SELF_DESCRIPTION, expected_status_code=200
        )
        try:
            self_description = SelfDescription.from_dict(rsp.json())
        except ValueError as ve:
            self_description = "error"
            logger.exception(f"Error creating SelfDescription: {ve}")

        return self_description

    @staticmethod
    def get_openapi_specs(external_self_description, api_version):
        """
        Get OpenAPI specs from an external connector self-description

        :param external_self_description: External connector self-description
        :param api_version: Data APP API version

        :return: OpenAPI specs
        """

        connector_id = external_self_description.id
        resource_catalog = external_self_description.catalogs

        endpoint_documentation_urls = []
        for resource in resource_catalog:
            if resource.id == (connector_id + ":data-app"):
                offered_resource = resource.offeredResource

                for off_res in offered_resource:
                    if off_res.path[-len(api_version) :] == api_version:
                        _openapi_url = off_res.documentation
                        _path = off_res.path
                        _agent = _path.split("/")[1:-1][0]
                        _version = _path.split("/")[-1]

                        try:
                            _endpoints = list(
                                requests.get(_openapi_url).json()["paths"].keys()
                            )
                        except Exception:
                            _endpoints = None

                        endpoint_documentation_urls.append(
                            {
                                "api_version": _version,
                                "agent": _agent,
                                "path": _agent,
                                "openapi_url": _openapi_url,
                                "endpoints": _endpoints,
                            }
                        )

        return endpoint_documentation_urls

    def openapi_request(
        self,
        external_access_url,
        data_app_agent_id,
        api_version,
        endpoint,
        params="",
        method="get",
        headers=None,
        data=None,
    ):
        """
        Execute an OpenAPI request to an external connector

        :param external_access_url: External access URL
        :param data_app_agent_id: Data App Agent (retrieved from path)
        :param api_version: External connector Data APP API version
        :param endpoint: Target external connector REST API server endpoint
        :param params: Request query parameters
        :param method: Request type (get, post, put, delete)
        :param headers: Request headers
        :param data: Request payload

        :return: Response object
        """

        _external_access_urll = f"{external_access_url}/router"

        _headers = {
            "Forward-AccessURL": _external_access_urll,
            "Forward-Sender": self.agent_id,
            "Forward-To": data_app_agent_id,
            "Forward-Recipient": data_app_agent_id,
        }

        if headers is None:
            headers = _headers
        else:
            headers.update(_headers)

        full_endpoint = f"{self.endpoints.OPEN_API}/{api_version}{endpoint}"

        rsp = ""
        if method == "get":
            rsp = self.controller.get(
                endpoint=full_endpoint, headers=headers, params=params
            )
        elif method == "post":
            rsp = self.controller.post(
                endpoint=full_endpoint, headers=headers, params=params, data=data
            )
        elif method == "put":
            rsp = self.controller.put(
                endpoint=full_endpoint, headers=headers, params=params, data=data
            )
        elif method == "delete":
            rsp = self.controller.delete(
                endpoint=full_endpoint, headers=headers, params=params
            )
        elif method == "patch":
            rsp = self.controller.patch(
                endpoint=full_endpoint, headers=headers, params=params, data=data
            )

        return rsp

    def query_metadata_broker(self):
        """
        Query the DS Metadata Broker for all registered connectors
        :return: Metadata Broker HTTP Response (JSON)
        """

        if not self.metadata_broker_url:
            raise Exception("No metadata broker url provided on " "TSGController init.")

        # Request data from DS Metadata Broker:
        rsp = self.controller.get(
            endpoint=self.endpoints.METADATA_BROKER_CONNECTORS,
            base_url=self.metadata_broker_url,
        )

        return rsp.json()

    def get_administrative_users(self):

        # Get the Administrative Users:
        rsp = self.controller.get(
            endpoint=self.endpoints.AUTH_USERS_MANAGER)
        
        return rsp.json()
    
    def new_administrative_user(self, id, password, roles):

        bytes = password.encode('utf-8')
        hash = bcrypt.hashpw(bytes, bcrypt.gensalt())

        headers = {
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            "id": id,
            "password": hash.decode('utf-8'),
            "roles": roles
        })

        # Register de new Administrative User:
        rsp = self.controller.post(
            endpoint=self.endpoints.AUTH_USERS_MANAGER,
            data=payload, headers=headers)

        if rsp.status_code == 200:
            return f"New Administrative User created with ID {id}"
        elif rsp.status_code == 500:
            return (f"Error creating Administrative User with ID {id}. One possible cause is that a user with ID {id} "
                    f"already exists.")

    def update_administrative_user(self, id, new_password, new_roles=None):

        headers = {
            'Content-Type': 'application/json'
        }

        endpoint = f"{self.endpoints.AUTH_USERS_MANAGER}/{id}"

        bytes = new_password.encode('utf-8')
        hash = bcrypt.hashpw(bytes, bcrypt.gensalt())
        payload = {
            'id': id,
            'password': hash.decode('utf-8')
        }

        if new_roles:
            payload['roles'] = new_roles

        # Delete an Administrative User:
        rsp = self.controller.put(
            endpoint=endpoint, data=json.dumps(payload), headers=headers)

        if rsp.status_code == 200:
            return f"Administrative User with ID {id} updated with success"

    def delete_administrative_user(self, id):

        endpoint = f"{self.endpoints.AUTH_USERS_MANAGER}/{id}"

        # Delete an Administrative User:
        rsp = self.controller.delete(
            endpoint=endpoint)

        if rsp.status_code == 200:
            return f"Administrative User with ID {id} deleted with success"
        elif rsp.status_code == 400:
            return f"Error: Administrative User with ID {id} not found."
        
    def get_catalog(self):
        """
        Get catalogs from the connector.
        """

        rsp = self.controller.get(
            endpoint=self.endpoints.RESOURCES, expected_status_code=200
        )
        catalogs_artifacts = []

        try:
            rsp_json = rsp.json()

            for catalogs_artifacts in rsp_json:
                catalogs_artifacts.append({'@type': catalogs_artifacts['@type'], '@id': catalogs_artifacts['@id']})

        except ValueError as ve:
            logger.exception(f"Error creating SelfDescription: {ve}")

        return catalogs_artifacts
    
    def delete_catalog(self, catalog_id):
        """
        Delete catalog from the connector.
        """

        endpoint = f"{self.endpoints.RESOURCES}/{catalog_id}"

        self.controller.delete(
            endpoint=endpoint, expected_status_code=200
        )
        