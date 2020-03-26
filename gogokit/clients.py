from uritemplate import URITemplate, expand
from .oauth import OAuthClient, OAuthTokenStore, OAuthToken
from .hal import HalClient
from .resources import *

class BaseClient(object):
	def __init__(self, hal, factory):
		self.hal = hal
		self.__factory = factory

	def __get_url(self, path, id):
		rootUrl = self.hal.get_root_url()
		template = URITemplate(rootUrl + path)

		return template.expand(id= str(id) if id is not None else "")

	def get_resource(self, path, id, params = None):
		url = self.__get_url(path, id)

		return self.hal.get_resource(url, self.__factory, params)

	def create(self, path, data, params = None):
		url = self.__get_url(path, None)
		
		return self.hal.post(url, data, self.__factory, params)

	def update(self, path, id, data, params = None):
		url = self.__get_url(path, id)
		return self.hal.patch(url, data, self.__factory, params)

	def upsert(self, path, id, data, params = None):
		url = self.__get_url(path, id)
		return self.hal.put(url, data, self.__factory, params)

	def delete(self, path, id, params = None):
		url = self.__get_url(path, id)

		return self.hal.delete(url, self.__factory, params)

	def get_resources(self, path, id, params = None):
		url = self.__get_url(path, id)
		
		return self.hal.get_paged_resource(url, self.__factory, params)
	
	def post_file(self, path, id, file_name, file, params = None):
		url = self.__get_url(path, id)
		return self.hal.post_file(url, file_name, file, self.__factory, params)

	def get_all_resources(self, path, id, params = None):
		params = {} if params is None else params
		params['page'] = 1
		params['page_size'] = 10000

		url = self.__get_url(path, id)

		result = []
		hasNextPage = True

		while hasNextPage:
			page = self.hal.get_paged_resource(url, self.__factory, params)

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

	def get_changed_resource(self, path, params = None):
		params = {} if params is None else params
		params['page'] = 1
		params['page_size'] = 10000

		if path.startswith('https'):
			url = path
		else:
			url = self.__get_url(path, id)

		result = []
		deleted_items =[]
		hasNextPage = True

		while hasNextPage:
			page = self.hal.get_changed_resource(url, self.__factory, params)

			if page.items:
				for item in page.items:
					result.append(item)
			
			if page.deleted_items:
				for item in page.deleted_items:
					deleted_items.append(item)

			if not "next" in page.links:
				hasNextPage = False
			else:
				url = page.links["next"].href

		page.items = result
		page.deleted_items = deleted_items

		return page

class SellerListingClient(BaseClient):
	PATH = 'sellerlistings{/id}'
	EXTERNALPATH = 'externalsellerlistings{/id}'

	def __init__(self, hal):
		super(SellerListingClient, self).__init__(hal, lambda data: SellerListing(data))

	def create_listing(self, data, params = None):
		return self.create(self.PATH, data, params)

	def get_listing(self, listingId, params = None):
		return self.get_resource(self.PATH, listingId, params)

	def get_all_listings(self, params = None):
		return self.get_resources(self.PATH, None, params)

	def get_changed_listings(self, nextLink, params = None):
		return self.get_changed_resource(nextLink or "sellerlistings?sort=resource_version", params)

	def update_listing(self, listingId, data, params = None):
		return self.update(self.PATH, listingId, data, params)

	def delete_listing(self, listingId, params = None):
		return self.delete(self.PATH, listingId, params)

	def get_listing_by_external_id(self, externalListingId, params = None):
		return self.get_resource(self.EXTERNALPATH, externalListingId, params)

	def update_listing_by_external_id(self, externalListingId, data, params = None):
		return self.update(self.EXTERNALPATH, externalListingId, data, params)

	def delete_listing_by_external_id(self, externalListingId, params = None):
		return self.delete(self.EXTERNALPATH, externalListingId, params)

class CountryClient(BaseClient):
	PATH = 'countries{/id}'

	def __init__(self, hal):
		super(CountryClient, self).__init__(hal, lambda data: Country(data))

	def get_country(self, countryCode, params = None):
		return self.get_resource(self.PATH, countryCode, params)

	def get_countries(self, params = None):
		return self.get_resources(self.PATH, None, params)

	def get_all_countries(self, params = None):
		return self.get_all_resources(self.PATH, None, params)

class CurrencyClient(BaseClient):
	PATH = 'currencies{/id}'

	def __init__(self, hal):
		super(CurrencyClient, self).__init__(hal, lambda data: Currency(data))

	def get_currency(self, currencyCode, params = None):
		return self.get_resource(self.PATH, currencyCode, params)

	def get_currencies(self, params = None):
		return self.get_resources(self.PATH, None, params)

	def get_all_currencies(self, params = None):
		return self.get_all_resources(self.PATH, None, params)

class LanguageClient(BaseClient):
	PATH = 'languages{/id}'

	def __init__(self, hal):
		super(LanguageClient, self).__init__(hal, lambda data: Language(data))
	
	def get_language(self, languageCode, params = None):
		return self.get_resource(self.PATH, languageCode, params)

	def get_languages(self, params = None):
		return self.get_resources(self.PATH, None, params)

	def get_all_languages(self, params = None):
		return self.get_all_resources(self.PATH, None, params)

class VenueClient(BaseClient):
	PATH = 'venues{/id}'

	def __init__(self, hal):
		super(VenueClient, self).__init__(hal, lambda data: Venue(data))

	def get_venue(self, venueId, params = None):
		return self.get_resource(self.PATH, venueId, params)

	def get_venues(self, params = None):
		return self.get_resources(self.PATH, None, params)

	def get_all_venues(self, params = None):
		return self.get_all_resources(self.PATH, None, params)

class MetroAreaClient(BaseClient):
	PATH = 'metroareas{/id}'

	def __init__(self, hal):
		super(MetroAreaClient, self).__init__(hal, lambda data: MetroArea(data))

	def get_metro_area(self, metroAreaCode, params = None):
		return self.get_resource(self.PATH, metroAreaCode, params)

	def get_metro_areas(self, params = None):
		return self.get_resources(self.PATH, None, params)

	def get_all_metro_areas(self, params = None):
		return self.get_all_resources(self.PATH, None, params)

class CategoryClient(BaseClient):
	PATH = 'categories{/id}'

	def __init__(self, hal):
		super(CategoryClient, self).__init__(hal, lambda data: Category(data))

	def get_category(self, categoryId, params = None):
		return self.get_resource(self.PATH, categoryId, params)

	def get_genres(self, params = None):
		return self.get_resources('categories/{id}/children?sort=name&direction=asc&embed=top_children', 0, params)

class EventClient(BaseClient):
	def __init__(self, hal):
		super(EventClient, self).__init__(hal, lambda data: Event(data))

	def get_event(self, eventId, params = None):
		return self.get_resource('events{/id}', eventId, params)

	def get_events_by_category(self, categoryId, params = None):
		return self.get_resources('categories/{id}/events', categoryId, params)

	def get_all_events_by_category(self, categoryId, params = None):
		return self.get_all_resources('categories/{id}/events', categoryId, params)

class ListingClient(BaseClient):
	def __init__(self, hal):
		super(ListingClient, self).__init__(hal, lambda data: Listing(data))

	def get_listing(self, listingId, params = None):
		return self.get_resource('listings{/id}', listingId, params)

	def get_listings_by_event(self, eventId, params = None):
		return self.get_resources('events/{id}/listings', eventId, params)

	def get_all_listings_by_event(self, eventId, params = None):
		return self.get_all_resources('events/{id}/listings', eventId, params)

class SearchClient(BaseClient):
	PATH = 'search'

	def __init__(self, hal):
		super(SearchClient, self).__init__(hal, lambda data: Search(data))

	def get_search_results(self, params):
		return self.get_resources(self.PATH, None, params)

	def get_all_search_results(self, params):
		return self.get_all_resources(self.PATH, None, params)

class ViagogoClient:
	def __init__(self, client_id = None, client_secret = None, oauth_token_store = None, env = "production"):
		self.__client_id = client_id
		self.__client_secret = client_secret
		self.__oauth_token_store = OAuthTokenStore() if oauth_token_store is None else oauth_token_store
		self.oauth = OAuthClient(client_id, client_secret, env)
		self.hal = HalClient(self.__oauth_token_store, env)
		self.event = EventClient(self.hal)
		self.listing = ListingClient(self.hal)
		self.sellerlisting = SellerListingClient(self.hal)
		self.category = CategoryClient(self.hal)
		self.search = SearchClient(self.hal)
		self.country = CountryClient(self.hal)
		self.currency = CurrencyClient(self.hal)
		self.language = LanguageClient(self.hal)
		self.venue = VenueClient(self.hal)
		self.metro_area = MetroAreaClient(self.hal)
		self.webhook = WebhookClient(self.hal)
		self.sale = SaleClient(self.hal)
		self.shipment = ShipmentClient(self.hal)
		self.ticketholder = TicketHolderClient(self.hal)
		self.eticket = ETicketClient(self.hal)

	def set_token(self, token):
		if token is None or isinstance(token, OAuthToken) == False:
			raise ValueError("You must provide an oauth token")
		return self.__oauth_token_store.set_token(token)


class WebhookClient(BaseClient):
	PATH = 'webhooks{/id}'
	def __init__(self, hal):
		super(WebhookClient, self).__init__(hal, lambda data: Webhook(data))

	def create_webhook(self, data, params = None):
		return self.create(self.PATH, data, params)

	def delete_webhook(self, webhookId, params = None):
		return self.delete(self.PATH, webhookId, params)

	def get_all_webhooks(self, params = None):
		return self.get_all_resources(self.PATH, params)


class SaleClient(BaseClient):
	PATH = 'sales{/id}'
	def __init__(self, hal):
		super(SaleClient, self).__init__(hal, lambda data: Sale(data))

	def get_all_sales(self,params = None):
		return self.get_all_resources(self.PATH, None, params)

	def get_sale(self, sale_id, params = None):
		return self.get_resource(self.PATH, sale_id, params)
	
	def confirm_sale(self, sale_id, params = None):
		return self.update(self.PATH, sale_id, {'confirmed':'true' }, params)
	
	def reject_sale(self, sale_id,  params = None):
		return self.update(self.PATH, sale_id, {'confirmed':'false' }, params)

	def change_ticket_type(self, sale_id, ticket_type, params = None):
		return self.update(self.PATH, sale_id, {'eticket_type': ticket_type}, params)

	def upload_eticket_urls(self, sale_id, eticket_urls, params = None):
		return self.update(self.PATH, sale_id, {'eticket_urls': eticket_urls}, params)

	def upload_transfer_confirmation(self, sale_id, transfer_confirmation_number, params = None):
		return self.update(self.PATH, sale_id, {'transfer_confirmation_number': transfer_confirmation_number}, params)

	def save_eticket_ids(self, sale_id, eticket_ids, params = None):
		return self.update(self.PATH, sale_id, {'eticket_ids': eticket_ids}, params)

class ShipmentClient(BaseClient):
	PATH = 'sales{/id}/shipments'
	def __init__(self, hal):
		super(ShipmentClient, self).__init__(hal, lambda data: Shipment(data))

	def get_shipment_label(self, url, params = None):
		return self.hal.get_file(url, params=params)
		
	def create_shipment(self, sale_id, params=None):
		return  self.upsert(self.PATH, sale_id, params)

class ETicketClient(BaseClient):
	PATH = 'sales{/id}/eticketuploads'
	def __init__(self, hal):
		super(ETicketClient, self).__init__(hal, lambda data: ETicketUpload(data))

	def upload_eticket(self, sale_id, file_name, file, params = None):
		return self.post_file(self.PATH, sale_id, file_name, file, params)
		
	def get_uploads(self, sale_id, params=None):
		return self.get_resources(self.PATH, sale_id, params)
		
class TicketHolderClient(BaseClient):
	PATH = 'sales{/id}/ticketholders'
	def __init__(self, hal):
		super(TicketHolderClient, self).__init__(hal, lambda data: TicketHolderDetail(data))

	def get_ticket_holder_details(self, sale_id, params = None):
		return self.get_all_resources(self.PATH, sale_id, params)
