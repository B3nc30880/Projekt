from flight import Flight

class Airline:
    def __init__(self, name: str):
        self.name = name
        self.flights = []

    def add_flight(self, flight: Flight):
        self.flights.append(flight)

    def get_flight_by_number(self, flight_number: str):
        for flight in self.flights:
            if flight.flight_number.upper() == flight_number.upper():
                return flight
        return None

    def list_flights(self):
        for flight in self.flights:
            print(flight)