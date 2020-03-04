from .hal import Resource
import iso8601

class Country(Resource):
	def __init__(self, data):
		super(Country, self).__init__(data)

		self.code = data.get("code", None)
		self.name = data.get("name", None)

class Language(Resource):
	def __init__(self, data):
		super(Language, self).__init__(data)
		self.code = data.get("code", None)
		self.name = data.get("name", None)

class Currency(Resource):
	def __init__(self, data):
		super(Currency, self).__init__(data)
		self.code = data.get("code", None)
		self.name = data.get("name", None)

class Venue(Resource):
	def __init__(self, data):
		super(Venue, self).__init__(data)
		self.id = data.get("id", None)
		self.name = data.get("name", None)

class MetroArea(Resource):
	def __init__(self, data):
		super(MetroArea, self).__init__(data)
		self.id = data.get("id", None)
		self.name = data.get("name", None)

class Event(Resource):
	def __init__(self, data):
		super(Event, self).__init__(data)
		self.id = data.get("id", None)
		self.name = data.get("name", None)
		self.start_date = iso8601.parse_date(data["start_date"]) if data.get("start_date", None) is not None else None
		self.date_confirmed = data.get("date_confirmed", None)
		self.end_date = iso8601.parse_date(data["end_date"]) if data.get("end_date", None) is not None else None
		self.notes_html = data.get("notes_html", None)
		self.restrictions_html = data.get("restrictions_html", None)
		self.min_ticket_price = MoneyFactory.create(data.get("min_ticket_price", None))

class Category(Resource):
	def __init__(self, data):
		super(Category, self).__init__(data)
		self.id = data.get("id", None)
		self.name = data.get("name", None)
		self.description_html = data.get("description_html", None)
		self.min_ticket_price = MoneyFactory.create(data.get("min_ticket_price", None))
		self.min_event_date = iso8601.parse_date(data["min_event_date"]) if data.get("min_event_date", None) is not None else None
		self.max_event_date = iso8601.parse_date(data["max_event_date"]) if data.get("max_event_date", None) is not None else None

class Search(Resource):
	def __init__(self, data):
		super(Search, self).__init__(data)
		self.title = data.get("title", None)
		self.type = data.get("type", None)
		self.type_description = data.get("type_description", None)
		self.category = data.get("category", None)
		self.event = data.get("event", None)
		self.venue = data.get("venue", None)

class Listing(Resource):
	def __init__(self, data):
		super(Listing, self).__init__(data)
		self.id = data.get("id", None)
		self.pickup_available = data.get("pickup_available", None)
		self.download_available = data.get("download_available", None)
		self.number_of_tickets = data.get("number_of_tickets", None)
		self.seating = data.get("seating", None)
		self.ticket_price = data.get("ticket_price", None)
		self.estimated_ticket_price = MoneyFactory.create(data.get("estimated_ticket_price", None))
		self.estimated_total_ticket_price = MoneyFactory.create(data.get("estimated_total_ticket_price", None))
		self.estimated_booking_fee = MoneyFactory.create(data.get("estimated_booking_fee", None))
		self.estimated_shipping = MoneyFactory.create(data.get("estimated_shipping", None))
		self.estimated_vat = MoneyFactory.create(data.get("estimated_vat", None))
		self.estimated_total_charge = MoneyFactory.create(data.get("estimated_total_charge", None))

class SellerListing(Resource):
	def __init__(self, data):
		super(SellerListing, self).__init__(data)
		self.id = data.get("id", None)
		self.created_at = iso8601.parse_date(data["created_at"])
		self.updated_at = iso8601.parse_date(data["updated_at"])
		self.external_id = data.get("external_id", None)
		self.expires_at = iso8601.parse_date(data["expires_at"]) if data.get("expires_at", None) is not None else None
		self.in_hand_at = iso8601.parse_date(data["in_hand_at"]) if data.get("in_hand_at", None) is not None else None
		self.number_of_tickets = data.get("number_of_tickets", None)
		self.display_number_of_tickets = data.get("display_number_of_tickets", None)
		self.seating = data.get("seating", None)
		self.display_seating = data.get("display_seating", None)
		self.ticket_price = MoneyFactory.create(data.get("ticket_price", None))
		self.ticket_proceeds = MoneyFactory.create(data.get("ticket_proceeds", None))
		self.face_value = MoneyFactory.create(data.get("face_value", None))
		self.instant_delivery = data.get("instant_delivery", None)
		if "_embedded" in data:
			self.event = data["_embedded"].get("event", None)
			self.split_type = data["_embedded"].get("split_type", None)
			self.ticket_type = data["_embedded"].get("ticket_type", None)
			self.venue = data["_embedded"].get("venue", None)

class Webhook(Resource):
	def __init__(self, data):
		super(Webhook, self).__init__(data)
		self.id = data.get("id", None)
		self.name = data.get("name", None)
		self.topics = data.get("topics", None)
		self.created_at = iso8601.parse_date(data["created_at"])

class Money(object):
	def __init__(self, data):
		self.amount = data.get("amount", None)
		self.currency_code = data.get("currency_code", None)
		self.display = data.get("display", None)

class Seating(object):
	def __init__(self, data):
		self.seat_to = data.get("seat_to", None)
		self.seat_from = data.get("seat_from", None)
		self.row = data.get("row", None)
		self.section = data.get("section", None)

class Sale(Resource):
	def __init__(self, data):
		super(Sale, self).__init__(data)
		self.id = data.get("id", None)
		self.created_at = iso8601.parse_date(data["created_at"])
		self.status = data.get("status", None)
		self.status_description = data.get("status_description", None)
		self.number_of_tickets = data.get("number_of_tickets", None)
		self.seating = data.get("seating", None)
		self.proceeds = MoneyFactory.create(data.get("proceeds", None))
		self.confirm_by = iso8601.parse_date(data["confirm_by"]) if data.get("confirm_by", None) is not None else None
		self.ship_by = iso8601.parse_date(data["ship_by"]) if data.get("ship_by", None) is not None else None
		self.payment_type = data.get("payment_type", None)
		self.payment_type_description = data.get("payment_type_description", None)
		self.extpayment_detailsrnal_id = data.get("payment_details", None)
	
		if "_embedded" in data:
			self.event = data["_embedded"].get("event", None)
			self.delivery_method = data["_embedded"].get("delivery_method", None)
			self.ticket_type = data["_embedded"].get("ticket_type", None)
			self.venue = data["_embedded"].get("venue", None)

class TicketHolderDetail(Resource):
	def __init__(self, data):
		super(TicketHolderDetail, self).__init__(data)
		self.name = data.get("full_name", None)
		self.email_address = data.get("email_address", None)

class ETicketUpload(Resource):
	def __init__(self, data):
		super(ETicketUpload, self).__init__(data)
		self.file_name = data.get("file_name", None)
		self.id = data.get("id", None)
		self.status_description = data.get("status_description", None)
		self.processed_at = iso8601.parse_date(data["processed_at"])
		self.original_number_of_tickets = data.get("original_number_of_tickets", None)
			
		if "_embedded" in data:
			self.etickets = list(map(lambda eticket: ETicket(eticket), data["_embedded"].get("etickets", None)))

class ETicket(Resource):
	def __init__(self, data):
		super(ETicket, self).__init__(data)
		self.file_name = data.get("file_name", None)
		self.id = data.get("id", None)
		if "_links" in data:
			self.delete_url = data["_links"].get("eticket:delete", None).get("href")
			self.document_url = data["_links"].get("eticket:document", None).get("href")

class Shipment(Resource):
	def __init__(self, data):
		super(Shipment, self).__init__(data)
		self.tracking_number = data.get("tracking_number", None)
		self.id = data.get("id", None)
		if "_links" in data:
			self.label_url = data["_links"].get("shipment:label", None).get("href")


class MoneyFactory:
	@staticmethod
	def create(data):
		if data is not None:
			return Money(data)
		return None