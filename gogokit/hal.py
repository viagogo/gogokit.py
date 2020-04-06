from .oauth import OAuthClient, OAuthTokenStore
from .http_client import HttpClient, HTTPBearerAuth
from .config import __enpoint_map__

import six

class Link(object):
	def __init__(self, data):		
		self.href = data["href"]
		self.title = data["title"]
		self.templated = data["templated"]

class Resource(object):
	def __init__(self, data):
		self.links = {}
		if "_links" in data:
			for rel, link in six.iteritems(data["_links"]):			
				self.links[rel] = Link(link)

class PagedResource(Resource):
	def __init__(self, data, factory):
		super(PagedResource, self).__init__(data)
		self.items = []
		for item in data["_embedded"]["items"]:
			self.items.append(factory(item))

		self.total_items = data["total_items"]
		self.page = data["page"]
		self.page_size = data["page_size"]


class ChangedResource(Resource):
	def __init__(self, data, factory):
		super(ChangedResource, self).__init__(data)
		self.items = []
		self.deleted_items = []
		
		for item in data["_embedded"]["items"]:
			self.items.append(factory(item))

		if "deleted_items" in data["_embedded"]:
			for item in data["_embedded"]["deleted_items"]:
				self.deleted_items.append(factory(item))

		self.total_items = data["total_items"]
		self.page = data["page"]
		self.page_size = data["page_size"]

class Root(Resource):
	def __init__(self, data):
		super(Root, self).__init__(data)
		self.__links_dict = {}
		for rel, link in six.iteritems(data["_links"]):			
			self.__links_dict[rel] = Link(link)

	def get_link(self, rel):
		return self.__links_dict[rel]


class HalClient:
	def __init__(self, token_store, env):
		if token_store is None or isinstance(token_store, OAuthTokenStore) == False:
			raise ValueError("You must provide an oauth token store")
		self.token_store = token_store
		self.root_url = __enpoint_map__.get(env)

	def get_root(self, params = None):
		return Root(HttpClient.get(self.root_url, auth=HTTPBearerAuth(self.token_store.get_access_token()), params= params))

	def get_root_url(self, params = None):
		return self.root_url

	def get_resource(self, url, factory, params = None):
		return factory(HttpClient.get(url, auth=HTTPBearerAuth(self.token_store.get_access_token()), params= params))

	def post(self, url, data,  factory, params = None):
		return factory(HttpClient.post(url, auth=HTTPBearerAuth(self.token_store.get_access_token()), json_data=data, params= params))

	def patch(self, url, data,  factory, params = None):
		return factory(HttpClient.patch(url, auth=HTTPBearerAuth(self.token_store.get_access_token()), json_data=data, params= params))

	def put(self, url, data, factory, params = None):
		return factory(HttpClient.put(url, auth=HTTPBearerAuth(self.token_store.get_access_token()), json_data=data,  params= params))

	def delete(self, url, factory, params = None):
		HttpClient.delete(url, auth=HTTPBearerAuth(self.token_store.get_access_token()), params= params)

	def get_paged_resources(self, url, factory, params = None):
		return PagedResource(HttpClient.get(url, auth=HTTPBearerAuth(self.token_store.get_access_token()), params= params), factory)

	def get_changed_resources(self, url, factory, params = None):
		return ChangedResource(HttpClient.get(url, auth=HTTPBearerAuth(self.token_store.get_access_token()), params= params), factory)

	def get_file(self, url, params = None):
		return HttpClient.get_file(url, auth=HTTPBearerAuth(self.token_store.get_access_token()), params= params)
        
	def post_file(self, url, file_name, file,  factory, params = None):
		return PagedResource(HttpClient.post_file(url, file_name, file, auth=HTTPBearerAuth(self.token_store.get_access_token()), params= params), factory)
