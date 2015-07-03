from .hal import Resource
import iso8601

class Country(Resource):
	def __init__(self, data):
		super(Country, self).__init__(data)

		self.code = data["code"]
		self.name = data["name"]

class Language(Resource):
	def __init__(self, data):
		super(Language, self).__init__(data)
		self.code = data["code"]
		self.name = data["name"]

class Currency(Resource):
	def __init__(self, data):
		super(Currency, self).__init__(data)
		self.code = data["code"]
		self.name = data["name"]

class Venue(Resource):
	def __init__(self, data):
		super(Venue, self).__init__(data)
		self.id = data["id"]
		self.name = data["name"]

class MetroArea(Resource):
	def __init__(self, data):
		super(MetroArea, self).__init__(data)
		self.id = data["id"]
		self.name = data["name"]

class Event(Resource):
	def __init__(self, data):
		super(Event, self).__init__(data)
		self.id = data["id"]
		self.name = data["name"]
		self.start_date = iso8601.parse_date(data["start_date"]) if data["start_date"] is not None else None
		self.date_confirmed = data["date_confirmed"]
		self.end_date = iso8601.parse_date(data["end_date"]) if data["end_date"] is not None else None
		self.notes_html = data["notes_html"]
		self.restrictions_html = data["restrictions_html"]
		self.min_ticket_price = MoneyFactory.create(data["min_ticket_price"])

class Category(Resource):
	def __init__(self, data):
		super(Category, self).__init__(data)
		self.id = data["id"]
		self.name = data["name"]
		self.description_html = data["description_html"]
		self.min_ticket_price = MoneyFactory.create(data["min_ticket_price"])
		self.min_event_date = iso8601.parse_date(data["min_event_date"]) if data["min_event_date"] is not None else None
		self.max_event_date = iso8601.parse_date(data["max_event_date"]) if data["max_event_date"] is not None else None

class Search(Resource):
	def __init__(self, data):
		super(Search, self).__init__(data)
		self.title = data["title"]
		self.type = data["type"]
		self.type_description = data["type_description"]
		self.category = data.get("category")
		self.event = data.get("event")
		self.venue = data.get("venue")

class Listing(Resource):
	def __init__(self, data):
		super(Listing, self).__init__(data)
		self.id = data["id"]
		self.pickup_available = data["pickup_available"]
		self.download_available = data["download_available"]
		self.number_of_tickets = data["number_of_tickets"]
		self.seating = data["seating"]
		self.ticket_price = data["ticket_price"]
		self.estimated_ticket_price = MoneyFactory.create(data["estimated_ticket_price"])
		self.estimated_total_ticket_price = MoneyFactory.create(data["estimated_total_ticket_price"])
		self.estimated_booking_fee = MoneyFactory.create(data["estimated_booking_fee"])
		self.estimated_shipping = MoneyFactory.create(data["estimated_shipping"])
		self.estimated_vat = MoneyFactory.create(data["estimated_vat"])
		self.estimated_total_charge = MoneyFactory.create(data["estimated_total_charge"])

class Money(object):
	def __init__(self, data):
		self.amount = data["amount"]
		self.currency_code = data["currency_code"]
		self.display = data["display"]

class Seating(object):
	def __init__(self, data):
		self.seat_to = data["seat_to"]
		self.seat_from = data["seat_from"]
		self.row = data["row"]
		self.section = data["section"]


class MoneyFactory:
	@staticmethod
	def create(data):
		if data is not None:
			return Money(data)
		return None