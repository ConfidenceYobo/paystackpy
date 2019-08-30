import os

import requests
import simplejson as json

from paystackpy.errors import *
import paystackpy.version as version


class APIConfig:
    """
    API configuration for paystackpy API wrapper
    """

    _CONTENT_TYPE = "application/json"
    _API_END_POINT = "https://api.paystack.co"

    def __init__(self, authorization_key=None):
        if authorization_key:
            self._PAYSTACK_AUTHORIZATION_KEY = authorization_key
        else:
            self._PAYSTACK_AUTHORIZATION_KEY = os.getenv('PAYSTACK_AUTHORIZATION_KEY', None)

        if not self._PAYSTACK_AUTHORIZATION_KEY:
            raise MissingAuthKeyError("Missing paystack Authorization key")

        self.request_headers = {
            "Authorization": "Bearer {0}".format(self._PAYSTACK_AUTHORIZATION_KEY),
            "Content-Type": "application/json",
            "user-agent": "PaystackPy - {0}".format(version.__version__)
        }

    def _url(self, path):
        return self._API_END_POINT + path

    def _parse_json(self, response_obj):
        parsed_response = response_obj.json()

        status = parsed_response.get('status', None)
        message = parsed_response.get('message', None)
        data = parsed_response.get('data', None)
        return response_obj.status_code, status, message, data

    def _handle_request(self, method, url, data=None):

        """
        Generic function to handle all API url calls
        Returns a python tuple of status code, status(bool), message, data
        """
        method_map = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'DELETE': requests.delete
        }

        payload = json.dumps(data) if data else data
        request = method_map.get(method)

        if not request:
            raise InvalidMethodError("Request method not recognised or implemented")

        response = request(url, headers=self.request_headers, data=payload, verify=True)
        if response.status_code == 404:
            return response.status_code, False, "The object request cannot be found", None

        if response.status_code in [200, 201]:
            return self._parse_json(response)
        else:
            body = response.json()
            return response.status_code, body.get('status'), body.get('message'), body.get('errors')}
