from typing import List
from typing import Any
from dataclasses import dataclass
from typing import Union


@dataclass
class OfferedResource:
    artifact_id: str
    contract_offer: str
    created: Union[str, None]
    access_url: str
    path: str
    documentation: str
    title: Union[str, None]
    description: Union[str, None]

    @staticmethod
    def from_dict(obj: Any) -> 'OfferedResource':
        if 'ids:resourceEndpoint' in obj.keys():
            # E.g., for data app's we do not have a ids:resourceEndpoint key
            _access_url = obj['ids:resourceEndpoint'][0]['ids:accessURL']['@id']
            path = obj['ids:resourceEndpoint'][0]['ids:path']
            access_url = _access_url + path
            documentation = obj['ids:resourceEndpoint'][0].get('ids:endpointDocumentation', [{'@id': ''}])[0]['@id']
        else:
            access_url = None
            path = None
            documentation = None

        contract_offer = str(obj.get('ids:contractOffer', [''])[0])
        created = str(obj.get("ids:created").get("@value")) if obj.get("ids:created") else None
        title = str(obj.get("ids:title")[0].get("@value")) if obj.get("ids:title") else None
        description = str(obj.get("ids:description")[0].get("@value")) if obj.get("ids:description") else None

        if contract_offer != "":
            artifact_id = obj['ids:representation'][0]['ids:instance'][0]['@id']
        else:
            artifact_id = obj['@id']

        return OfferedResource(artifact_id, contract_offer, created,
                               access_url, path, documentation, title,
                               description)

    def to_dict(self) -> dict:
        return {
            "artifact_id": self.artifact_id,
            "contract_offer": self.contract_offer,
            "created": self.created,
            "access_url": self.access_url,
            "path": self.path,
            "documentation": self.documentation,
            "title": self.title,
            "description": self.description,
        }


@dataclass
class ResourceCatalog:
    id: str
    offeredResource: List[OfferedResource]

    @staticmethod
    def from_dict(obj: Any) -> 'ResourceCatalog':
        _id = str(obj.get("@id"))
        _offeredResource = [OfferedResource.from_dict(y) for y in obj.get("ids:offeredResource")]
        return ResourceCatalog(_id, _offeredResource)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "offeredResource": [x.to_dict() for x in self.offeredResource],
        }


@dataclass(frozen=True)
class SelfDescription:
    id: str
    title: str
    description: str
    securityProfile: str
    curator: str
    maintainer: str
    endpoints: str
    catalogs: List['ResourceCatalog']

    @staticmethod
    def from_dict(obj: Any) -> 'SelfDescription':
        """
        Converts self-description dictionary into a SelfDescription object
        with some of the most relevant fields.

        :param obj: self-description dictionary
        :return: SelfDescription object
        """

        try:
            _id = str(obj.get("@id"))
            _title = str(obj.get("ids:title")[0].get("@value"))
            _description = str(obj.get("ids:description")[0].get("@value"))
            _security_profile = str(obj.get("ids:securityProfile").get("@id"))
            _curator = str(obj.get("ids:curator").get("@id"))
            _maintainer = str(obj.get("ids:maintainer").get("@id"))
            _endpoints = str(obj.get("ids:hasDefaultEndpoint").get("ids:accessURL").get("@id"))
            resource_catalogs = obj.get("ids:resourceCatalog", [])
            _catalogs = [ResourceCatalog.from_dict(y) for y in resource_catalogs] if resource_catalogs else []
            return SelfDescription(_id, _title, _description, _security_profile, _curator, _maintainer, _endpoints,
                                   _catalogs)
        except (KeyError, AttributeError, IndexError) as e:
            raise ValueError(f"Error creating SelfDescription: {e}")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "securityProfile": self.securityProfile,
            "curator": self.curator,
            "maintainer": self.maintainer,
            "endpoints": self.endpoints,
            "catalogs": [x.to_dict() for x in self.catalogs],
        }
