from airline import Airline
from flight import DomesticFlight, InternationalFlight
from booking import Booking
from datetime import date
from utils import parse_date, normalize_flight_number

class BookingSystem:
    def __init__(self):
        self.airline = Airline("Python Airways")
        self.bookings = []
        self._init_data()

    def _init_data(self):
        f1 = DomesticFlight("BUD101", "Budapest", 10000, 6)
        f2 = InternationalFlight("LON201", "London", 25000, 5)
        f3 = InternationalFlight("NYC301", "New York", 70000, 5)
        f4 = InternationalFlight("BER401", "Berlin", 22000, 4)
        f5 = DomesticFlight("ROM501", "Róma", 15000, 4)
        self.airline.add_flight(f1)
        self.airline.add_flight(f2)
        self.airline.add_flight(f3)
        self.airline.add_flight(f4)
        self.airline.add_flight(f5)
        self._add_booking("Kiss Anna", f1, "2025-06-08")
        self._add_booking("Nagy Béla", f1, "2025-06-10")
        self._add_booking("Kiss Anna", f2, "2025-07-01")
        self._add_booking("Kovács Péter", f3, "2025-07-05")
        self._add_booking("Tóth Eszter", f2, "2025-07-10")
        self._add_booking("Szabó János", f3, "2025-08-01")

    def _add_booking(self, passenger, flight, departure):
        if flight.book_seat():
            self.bookings.append(Booking(passenger, flight, departure))

    def list_bookings(self):
        if not self.bookings:
            print("Nincs foglalás.")
        for i, booking in enumerate(self.bookings, start=1):
            print(f"{i}. {booking}")

    def list_flights(self):
        self.airline.list_flights()

    def get_flight_by_number(self, flight_number):
        norm = normalize_flight_number(flight_number)
        for f in self.airline.flights:
            if normalize_flight_number(f.flight_number) == norm:
                return f
        return None

    def book_ticket(self):
        print("=== Jegyfoglalás ===")
        if not self.airline.flights:
            print("Nincs elérhető járat!")
            return
        self.list_flights()
        flight_number = input("Add meg a járatszámot: ").strip()
        flight = self.get_flight_by_number(flight_number)
        if not flight:
            print("Nincs ilyen járat.")
            return
        if not flight.is_available():
            print("A járatra minden hely elkelt!")
            return
        passenger = input("Név: ").strip()
        departure_str = input("Indulás dátuma: ").strip()
        try:
            departure_date = parse_date(departure_str)
            if departure_date < date.today():
                print("Az indulás dátuma nem lehet múltbeli!")
                return
        except Exception:
            print("Hibás dátum formátum.")
            return

        if flight.book_seat():
            booking = Booking(passenger, flight, departure_date)
            self.bookings.append(booking)
            print(f"Foglalás sikeres! Ár: {flight.get_price()} Ft")
        else:
            print("A járatra már nem foglalható több jegy.")

    def cancel_booking(self):
        print("=== Foglalás lemondása ===")
        if not self.bookings:
            print("Nincs foglalás.")
            return
        self.list_bookings()
        idx = input("Add meg a lemondandó foglalás sorszámát: ").strip()
        try:
            idx = int(idx)
            if idx < 1 or idx > len(self.bookings):
                raise ValueError
            booking = self.bookings[idx-1]
            booking.flight.cancel_seat()
            del self.bookings[idx-1]
            print("Foglalás törölve.")
        except Exception:
            print("Érvénytelen sorszám.")

    def run(self):
        while True:
            print(f"\n--- Jegyfoglaló rendszer | Légitársaság: {self.airline.name} ---")
            print("1. Foglalások listázása")
            print("2. Járatok listázása")
            print("3. Jegy foglalása")
            print("4. Foglalás lemondása")
            print("5. Kilépés")
            choice = input("Válassz: ")
            if choice == "1":
                self.list_bookings()
            elif choice == "2":
                self.list_flights()
            elif choice == "3":
                self.book_ticket()
            elif choice == "4":
                self.cancel_booking()
            elif choice == "5":
                break
            else:
                print("Érvénytelen menüpont!")