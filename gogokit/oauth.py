import requests

from .http_client import HttpClient
from requests.auth import HTTPBasicAuth
from .config import __auth_endpoint_map__

class OAuthToken(object):
	def __init__(self, data):
		self.__dict__ = data

class OAuthTokenStore:
	def __init__(self, token = None):
		self.token = token
		
	def set_token(self, token):
		self.token = token

	def get_access_token(self):
		return self.token

class OAuthClient:
	def __init__(self, client_id, client_secret, env):
		self.client_id = client_id
		self.client_secret = client_secret
		self.token_url = __auth_endpoint_map__.get(env)

	def get_client_access_token(self, scopes = None):
		data = {'grant_type': 'client_credentials', 'scope': scopes}
		return OAuthToken(HttpClient.post(self.token_url, data = data, auth=HTTPBasicAuth(self.client_id, self.client_secret)))

	def get_password_access_token(self, login, password, scopes):
		data = {'grant_type': 'password','username':login, 'password':password, 'scope': scopes};
		return OAuthToken(HttpClient.post(self.token_url, data = data, auth=HTTPBasicAuth(self.client_id, self.client_secret)))

	def get_refresh_token(self, refresh_token):
		data = {'grant_type': 'refresh_token','refresh_token': refresh_token};
		return OAuthToken(HttpClient.post(self.token_url, data = data, auth=HTTPBasicAuth(self.client_id, self.client_secret)))
			
	def set_access_token(self, access_token):
		token = {'access_token': access_token} 
		return OAuthToken(token)

