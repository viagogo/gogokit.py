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


class MoneyFactory:
	@staticmethod
	def create(data):
		if data is not None:
			return Money(data)
		return None