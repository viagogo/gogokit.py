import requests
import json
from exceptions import HttpError 

class HTTPBearerAuth(requests.auth.AuthBase):
     def __init__(self, token):
     	self.token = token

     def __call__(self, request):
     	request.headers["Authorization"] = "Bearer " + self.token.access_token
        return request

class HttpClient:
	@staticmethod
	def get(url, auth, data = None, params = None, headers = None):
		response = requests.get(url, data = data, params = params, headers = headers, auth=auth)
		HttpClient.__validate_response(response)
		return json.loads(response.text)

	@staticmethod
	def post(url, auth, data = None, params = None, headers = None):
		response = requests.post(url, data, params = params, headers = headers, auth=auth)
		HttpClient.__validate_response(response)
		return json.loads(response.text)

	@staticmethod
	def put(url, auth, data = None, params = None, headers = None):
		response = requests.put(url, data, params = params, headers = headers, auth=auth)
		HttpClient.__validate_response(response)
		return json.loads(response.text)

	@staticmethod
	def patch(url, auth, data = None, params = None, headers = None):
		response = requests.patch(url, data, params = params, headers = headers, auth=auth)
		HttpClient.__validate_response(response)
		return json.loads(response.text)

	@staticmethod
	def __validate_response(response):
			if response.status_code >= 400:
				error = json.loads(response.text) if response.text is not None else {}
				raise HttpError({"status_code": response.status_code, "reason": response.reason, "error": error})