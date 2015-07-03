from .oauth import OAuthClient, OAuthTokenStore
from .hal import HalClient
from .resources import *

class BaseClient(object):
	def __init__(self, hal_client, factory):
		self.hal_client = hal_client
		self.__factory = factory

	def get_resource(self, linkRel, linkParams, params = None):
		root = self.hal_client.get_root()
		url = root.get_link(linkRel).href + '/' + str(linkParams)
		
		return self.hal_client.get_resource(url, self.__factory, params)

	def get_resources(self, linkRel, linkParams, params = None):
		root = self.hal_client.get_root()
		linkParams = '/' + str(linkParams) if linkParams is not None else ''
		url = root.get_link(linkRel).href + linkParams
		
		return self.hal_client.get_paged_resource(url, self.__factory, params)

	def get_all_resources(self, linkRel, linkParams, params = None):
		params = {} if params is None else params
		params['page'] = 1
		params['page_size'] = 1000

		root = self.hal_client.get_root()
		linkParams = '/' + str(linkParams) if linkParams is not None else ''
		url = root.get_link(linkRel).href + linkParams

		result = []
		hasNextPage = True

		while hasNextPage:
			page = self.hal_client.get_paged_resource(url, self.__factory, params)

			if page.items:
				for item in page.items:
					result.append(item)
			else:
				break			

			if not "next" in page.links:
				hasNextPage = False
			else:
				url = page.links["next"].href

		return result

class CountryClient(BaseClient):
	REL = 'viagogo:countries'

	def __init__(self, hal_client):
		super(CountryClient, self).__init__(hal_client, lambda data: Country(data))

	def get_country(self, countryCode, params = None):
		return self.get_resource(self.REL, countryCode, params)

	def get_countries(self, params = None):
		return self.get_resources(self.REL, None, params)

	def get_all_countries(self, params = None):
		return self.get_all_resources(self.REL, None, params)

class CurrencyClient(BaseClient):
	REL = 'viagogo:currencies'

	def __init__(self, hal_client):
		super(CurrencyClient, self).__init__(hal_client, lambda data: Currency(data))

	def get_currency(self, currencyCode, params = None):
		return self.get_resource(self.REL, currencyCode, params)

	def get_currencies(self, params = None):
		return self.get_resources(self.REL, None, params)

	def get_all_currencies(self, params = None):
		return self.get_all_resources(self.REL, None, params)

class LanguageClient(BaseClient):
	REL = 'viagogo:languages'

	def __init__(self, hal_client):
		super(LanguageClient, self).__init__(hal_client, lambda data: Language(data))
	
	def get_language(self, languageCode, params = None):
		return self.get_resource(self.REL, languageCode, params)

	def get_languages(self, params = None):
		return self.get_resources(self.REL, None, params)

	def get_all_languages(self, params = None):
		return self.get_all_resources(self.REL, None, params)

class VenueClient(BaseClient):
	REL = 'viagogo:venues'

	def __init__(self, hal_client):
		super(VenueClient, self).__init__(hal_client, lambda data: Venue(data))

	def get_venue(self, venueId, params = None):
		return self.get_resource(self.REL, venueId, params)

	def get_venues(self, params = None):
		return self.get_resources(self.REL, None, params)

	def get_all_venues(self, params = None):
		return self.get_all_resources(self.REL, None, params)

class MetroAreaClient(BaseClient):
	REL = 'viagogo:metroareas'

	def __init__(self, hal_client):
		super(MetroAreaClient, self).__init__(hal_client, lambda data: MetroArea(data))

	def get_metro_area(self, metroAreaCode, params = None):
		return self.get_resource(self.REL, metroAreaCode, params)

	def get_metro_areas(self, params = None):
		return self.get_resources(self.REL, None, params)

	def get_all_metro_areas(self, params = None):
		return self.get_all_resources(self.REL, None, params)

class CategoryClient(BaseClient):
	REL = 'viagogo:genres'

	def __init__(self, hal_client):
		super(CategoryClient, self).__init__(hal_client, lambda data: Category(data))

	def get_category(self, categoryId, params = None):
		return self.get_resource('self', 'categories/' + str(categoryId), params)

	def get_genres(self, params = None):
		return self.get_resources(self.REL, None, params)

class EventClient(BaseClient):
	def __init__(self, hal_client):
		super(EventClient, self).__init__(hal_client, lambda data: Event(data))

	def get_event(self, eventId, params = None):
		return self.get_resource('self', 'events/' + str(eventId), params)

	def get_events_by_category(self, categoryId, params = None):
		return self.get_resources('self', 'categories/' + str(categoryId) + '/events/', params)

	def get_all_events_by_category(self, categoryId, params = None):
		return self.get_all_resources('self', 'categories/' + str(categoryId) + '/events/', params)

class ListingClient(BaseClient):
	def __init__(self, hal_client):
		super(ListingClient, self).__init__(hal_client, lambda data: Listing(data))

	def get_listing(self, eventId, params = None):
		return self.get_resource('self', 'listings/' + str(eventId), params)

	def get_listings_by_event(self, eventId, params = None):
		return self.get_resources('self', 'events/' + str(eventId) + '/listings/', params)

	def get_all_listings_by_event(self, eventId, params = None):
		return self.get_all_resources('self', 'events/' + str(eventId) + '/listings/', params)

class SearchClient(BaseClient):
	REL = 'viagogo:search'

	def __init__(self, hal_client):
		super(SearchClient, self).__init__(hal_client, lambda data: Search(data))

	def get_search_results(self, params):
		return self.get_resources(self.REL, None, params)

	def get_all_search_results(self, params):
		return self.get_all_resources(self.REL, None, params)

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
		self.metro_area_client = MetroAreaClient(self.hal_client)

	def set_token(self, token):
		return self.__oauth_token_store.set_token(token)