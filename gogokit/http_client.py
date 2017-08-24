import requests
import json
from .exceptions import HttpError 

from pprint import pprint

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
	def post(url, data, auth , params = None, headers = None):
		response = requests.post(url, json=data, params = params, headers = headers, auth=auth)
		HttpClient.__validate_response(response)
		return json.loads(response.text)

	@staticmethod
	def put(url, data, auth, params = None, headers = None):
		response = requests.put(url, json=data, params = params, headers = headers, auth=auth)
		HttpClient.__validate_response(response)
		return json.loads(response.text)

	@staticmethod
	def patch(url, data, auth, params = None, headers = None):
		response = requests.patch(url, json=data, params = params, headers = headers, auth=auth)
		HttpClient.__validate_response(response)
		return json.loads(response.text)

	@staticmethod
	def delete(url, auth, params = None, headers = None):		
		response = requests.delete(url, data = None, params = params, headers = headers, auth=auth)
		HttpClient.__validate_response(response)

	@staticmethod
	def __validate_response(response):
			error = None
			if response.status_code >= 400:
				try:
					error = json.loads(response.text)
				except Exception as e:
					pass
			
				raise HttpError({"status_code": response.status_code, "reason": response.reason, "error": error})

				  