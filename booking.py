class Booking:
    def __init__(self, passenger_name: str, flight, departure_date):
        self.passenger_name = passenger_name
        self.flight = flight
        self.departure_date = departure_date

    def __str__(self):
        return (f"Utazó: {self.passenger_name} | Járat: {self.flight.flight_number} | "
                f"Cél: {self.flight.destination} | Indulás: {self.departure_date} | "
                f"Ár: {self.flight.get_price()} Ft")