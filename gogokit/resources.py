from hal import Resource

class Country(Resource):
	def __init__(self, data):
		super(Country, self).__init__(data)

		self.code = data["code"]
		self.name = data["name"]

class Language(Resource):
	def __init__(self, data):
		self.code = data["code"]
		self.name = data["name"]

class Currency(Resource):
	def __init__(self, data):
		self.code = data["code"]
		self.name = data["name"]

class Venue(Resource):
	def __init__(self, data):
		self.id = data["id"]
		self.name = data["name"]

class MetroArea(Resource):
	def __init__(self, data):
		self.id = data["id"]
		self.name = data["name"]

class Event(Resource):
	def __init__(self, data):
		self.code = data["id"]
		self.name = data["name"]

class Category(Resource):
	def __init__(self, data):
		self.code = data["id"]
		self.name = data["name"]

class Listing(Resource):
	def __init__(self, data):
		self.code = data["id"]
		self.name = data["name"]
		self.pickup_available = data["pickup_available"]
		self.download_available = data["download_available"]
		self.number_of_tickets = data["number_of_tickets"]
		self.seating = data["seating"]
		self.ticket_price = data["ticket_price"]
		self.estimated_ticket_price = Money(data["estimated_ticket_price"])
		self.estimated_total_ticket_price = Money(data["estimated_total_ticket_price"])
		self.estimated_booking_fee = Money(data["estimated_booking_fee"])
		self.estimated_shipping = Money(data["estimated_shipping"])
		self.estimated_vat = Money(data["estimated_vat"])
		self.estimated_total_charge = Money(data["estimated_total_charge"])

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