from oauth import OAuthClient
from http_client import HttpClient, HTTPBearerAuth
from config import __root_url__

class Link(object):
	def __init__(self, data):		
		self.href = data["href"]
		self.title = data["title"]
		self.templated = data["templated"]

class Resource(object):
	def __init__(self, data):
		self.links = {}
		for rel, link in data["_links"].iteritems():			
			self.links[rel] = Link(link)

class PagedResource(Resource):
	def __init__(self, data, factory):
		self.items = []
		for item in data["_embedded"]["items"]:
			self.items.append(factory(item))

		self.total_items = data["total_items"]
		self.page = data["page"]
		self.page_size = data["page_size"]

class Root(Resource):
	def __init__(self, data):
		super(Root, self).__init__(data)
		self.__links_dict = {}
		for rel, link in data["_links"].iteritems():			
			self.__links_dict[rel] = Link(link)

		self.self_link = Link(data["_links"]["self"])

	def get_link(self, rel):
		return self.__links_dict[rel]


class HalClient:
	def __init__(self, token_store):
		if token_store is None:
			raise ValueError("You must provide a token store")
		self.token_store = token_store

	def get_root(self, params = None):
		return Root(HttpClient.get(__root_url__, auth=HTTPBearerAuth(self.token_store.get_access_token()), params= params))

	def get_resource(self, url, factory, params = None):
		return factory(HttpClient.get(url, auth=HTTPBearerAuth(self.token_store.get_access_token()), params= params))

	def get_paged_resource(self, url, factory, params = None):
		return PagedResource(HttpClient.get(url, auth=HTTPBearerAuth(self.token_store.get_access_token()), params= params), factory)