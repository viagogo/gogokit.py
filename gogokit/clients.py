from oauth import OAuthClient, OAuthTokenStore
from hal import HalClient
from resources import *

class BaseClient(object):
	def __init__(self, hal_client, factory):
		self.hal_client = hal_client
		self.__factory = factory

	def get_resource_from_root(self, linkRel, linkParams, params = None):
		root = self.hal_client.get_root()
		url = root.get_link(linkRel).href + '/' + linkParams
		
		return self.hal_client.get_resource(url, self.__factory, params)

	def get_resources_from_root(self, linkRel, linkParams, params = None):
		root = self.hal_client.get_root()
		url = root.get_link(linkRel).href
		
		return self.hal_client.get_paged_resource(url, self.__factory, params)

class CountryClient(BaseClient):
	REL = 'viagogo:countries'

	def __init__(self, hal_client):
		super(CountryClient, self).__init__(hal_client, lambda data: Country(data))

	def get_country(self, countryCode, params = None):
		return self.get_resource_from_root(REL, countryCode, params = params)

	def get_countries(self, params = None):
		return self.get_resources_from_root(REL, None, params = params)

class CurrencyClient(BaseClient):
	def __init__(self, hal_client):
		super(CurrencyClient, self).__init__(hal_client, lambda data: Country(data))

class LanguageClient(BaseClient):
	def __init__(self, hal_client):
		super(LanguageClient, self).__init__(hal_client, lambda data: Language(data))

class VenueClient(BaseClient):
	def __init__(self, hal_client):
		super(VenueClient, self).__init__(hal_client, lambda data: Venue(data))

class MetroAreaClient(BaseClient):
	def __init__(self, hal_client):
		super(MetroAreaClient, self).__init__(hal_client, lambda data: MetroArea(data))

class CategoryClient(BaseClient):
	def __init__(self, hal_client):
		super(CategoryClient, self).__init__(hal_client, lambda data: Category(data))

class EventClient(BaseClient):
	def __init__(self, hal_client):
		super(EventClient, self).__init__(hal_client, lambda data: Event(data))

class ListingClient(BaseClient):
	def __init__(self, hal_client):
		super(ListingClient, self).__init__(hal_client, lambda data: Listing(data))

class SearchClient(BaseClient):
	def __init__(self, hal_client):
		super(SearchClient, self).__init__(hal_client, lambda data: Search(data))


class ViagogoClient:
	def __init__(self, client_id, client_secret, oauth_token_store = None):
		self.__client_id = client_id
		self.__client_secret = client_secret
		self.__oauth_token_store = OAuthTokenStore() if oauth_token_store is None else oauth_token_store
		self.oauth_client = OAuthClient(client_id, client_secret)
		self.hal_client = HalClient(self.__oauth_token_store)
		self.event_client = EventClient(self.hal_client)
		self.listing_client = ListingClient(self.hal_client)
		self.category_client = CategoryClient(self.hal_client)
		self.search_client = SearchClient(self.hal_client)
		self.country_client = CountryClient(self.hal_client)
		self.currency_client = CurrencyClient(self.hal_client)
		self.language_client = LanguageClient(self.hal_client)
		self.venue_client = VenueClient(self.hal_client)

	def set_token(self, token):
		return self.__oauth_token_store.set_token(token)