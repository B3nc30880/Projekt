from abc import ABC, abstractmethod

class Flight(ABC):
    def __init__(self, flight_number: str, destination: str, base_price: int, seats: int):
        self.flight_number = flight_number
        self.destination = destination
        self.base_price = base_price
        self.seats = seats
        self.booked_seats = 0

    @abstractmethod
    def get_price(self):
        pass

    def is_available(self):
        return self.booked_seats < self.seats

    def book_seat(self):
        if self.is_available():
            self.booked_seats += 1
            return True
        return False

    def cancel_seat(self):
        if self.booked_seats > 0:
            self.booked_seats -= 1
            return True
        return False

    def __str__(self):
        return f"Járatszám: {self.flight_number}, Cél: {self.destination}, Ár: {self.get_price()} Ft, Szabad/foglalt: {self.seats-self.booked_seats}/{self.seats}"

class DomesticFlight(Flight):
    def get_price(self):
        return int(self.base_price * 0.8)

class InternationalFlight(Flight):
    def get_price(self):
        return int(self.base_price * 1.5)