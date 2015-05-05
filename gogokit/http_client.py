import requests
import json

class HTTPBearerAuth(requests.auth.AuthBase):
     def __init__(self, token):
     	self.token = token

     def __call__(self, request):
     	request.headers["Authorization"] = "Bearer " + self.token
        return request

class HttpClient:
	@staticmethod
	def get(url, data = None, params = None, headers = None, auth):
		response = requests.get(url, data = data, params = params, headers = headers, auth)

		return json.loads(response.text)

	@staticmethod
	def post(url, data = None, params = None, headers = None, auth):
		response = requests.post(url, data, params = params, headers = headers, auth)

		return json.loads(response.text)

	@staticmethod
	def put(url, data = None, params = None, headers = None, auth):
		response = requests.put(url, data, params = params, headers = headers, auth)

		return json.loads(response.text)

	@staticmethod
	def patch(url, data = None, params = None, headers = None, auth):
		response = requests.patch(url, data, params = params, headers = headers, auth)

		return json.loads(response.text)