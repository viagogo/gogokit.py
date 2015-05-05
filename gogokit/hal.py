from oauth import OauthClient
from http_client import HttpClient, HTTPBearerAuth
from config import __root_url__

class HalClient:
	def __init__(self, token_store = None):
		if token_store is None:
			raise ValueError("You must provide a token store")
		self.token_store = token_store

	def get_root(self, params):
		return Root(HttpClient.get(__root_url__, params= params, auth=HTTPBearerAuth(self.token_store.get_access_token())))

	def get_resource(self, url, params):
		return HttpClient.get(url, auth=HTTPBearerAuth(self.token_store.get_access_token()))

class Link(object):
	def __init__(self, data):
		self.href = data["href"]
		self.title = data["title"]
		self.templated = data["templated"]

class Resource(object):
	def __init__(self, data):
		self.links = []
		for link in links:
			self.links.append(Link(link))

		self.self_link = Link(data["_links"]["self"])

class PagedResource(Resource):
	def __init__(self, data, factory):
		self.items = []
		for item in data["_embedded"]["items"]:
			self.items.append(factory(item))

		self.total_items = data["total_items"]
		self.page = data["page"]
		self.page_size = data["page_size"]


