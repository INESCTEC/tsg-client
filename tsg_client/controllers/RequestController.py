"""

This is a generic request controller. It is responsible for the communication
between the server and the client. You don't need to make changes to the
RequestController class, but you can if you want to. Make sure those changes
reflect a general purpose that can solve other similar problems and not a
specific one. The only thing you need to do is to change the base URL in the
external_open_api_request.py file to match your server.

Continue the work in the external_open_api_request.py file. You can use the RequestController class
to make requests to the server. You may create helper functions in other files
that can also meet general problem-solving.

author: andre.f.garcia@inesctec.pt

"""

import requests

from loguru import logger


class RequestController:
    # Set to True if you want to verify the SSL certificate or None to ignore
    verify = True

    def __init__(self, base_url, api_key, connector_id, agent_id=None):
        self.base_url = base_url
        self.api_key = api_key
        self.connector_id = connector_id
        self.agent_id = agent_id
        self.headers = {'Authorization': 'Bearer ' + api_key}
        self.session = requests.Session()  # A session to persist parameters

    def request(self, method, endpoint,
                params=None, data=None,
                files=None,
                expected_status_code=None,
                headers=None,
                base_url=None,
                **kwargs):

        if headers is None:
            headers = self.headers

        if base_url is None:
            base_url = self.base_url

        url = f"{base_url}/{endpoint}"
        logger.debug(f"method: {method} "
                     f"| url: {url} "
                     f"| params: {kwargs} "
                     f"| headers: {headers}")
        response = self.session.request(method, url,
                                        verify=self.verify,
                                        params=params,
                                        data=data,
                                        headers=headers,
                                        files=files,
                                        **kwargs)

        logger.debug(f"method: {method} "
                     f"| url: {url} "
                     f"| params: {kwargs} "
                     f"| headers: {headers} "
                     f"| status: {response.status_code}")

        if expected_status_code and response.status_code != expected_status_code:
            raise Exception(f"Expected status_code {expected_status_code}, "
                            f"but got {response.status_code},"
                            f"response {response.content}")

        return response

    def get(self, endpoint, **kwargs):
        return self.request('GET', endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request('POST', endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request('PUT', endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request('DELETE', endpoint, **kwargs)
