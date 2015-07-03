import requests

from .http_client import HttpClient
from requests.auth import HTTPBasicAuth
from .config import __token_url__

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
	def __init__(self, client_id, client_secret):
		self.client_id = client_id
		self.client_secret = client_secret

	def get_client_access_token(self, scopes = None):
		data = {'grant_type': 'client_credentials', 'scope': scopes}
		return OAuthToken(HttpClient.post(__token_url__, data = data, auth=HTTPBasicAuth(self.client_id, self.client_secret)))

	def get_password_access_token(self, login, password, scopes):
		data = {'grant_type': 'password','username':login, 'password':password, 'scope': scopes};
		return OAuthToken(HttpClient.post(__token_url__, data = data, auth=HTTPBasicAuth(self.client_id, self.client_secret)))

	def get_refresh_token(self, refresh_token):
		data = {'grant_type': 'refresh_token','refresh_token': refresh_token};
		return OAuthToken(HttpClient.post(__token_url__, data = data, auth=HTTPBasicAuth(self.client_id, self.client_secret)))
