class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Room {self.room_number} ({self.room_type}): ${self.price:.2f} - {status}"


class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room_number, room_type, price):
        room = Room(room_number, room_type, price)
        self.rooms.append(room)
        print(f"Added {room}")

    def check_availability(self):
        available_rooms = [room for room in self.rooms if not room.is_booked]
        if not available_rooms:
            print("No available rooms.")
        else:
            for room in available_rooms:
                print(room)

    def book_room(self, room_number):
        room = next((room for room in self.rooms if room.room_number == room_number), None)
        if room:
            if not room.is_booked:
                room.is_booked = True
                print(f"Room {room_number} has been booked.")
            else:
                print(f"Room {room_number} is already booked.")
        else:
            print(f"Room {room_number} not found.")

    def cancel_booking(self, room_number):
        room = next((room for room in self.rooms if room.room_number == room_number), None)
        if room:
            if room.is_booked:
                room.is_booked = False
                print(f"Booking for room {room_number} has been canceled.")
            else:
                print(f"Room {room_number} is not booked.")
        else:
            print(f"Room {room_number} not found.")

    def modify_room(self, room_number, new_room_type=None, new_price=None):
        room = next((room for room in self.rooms if room.room_number == room_number), None)
        if room:
            if new_room_type:
                room.room_type = new_room_type
            if new_price:
                room.price = new_price
            print(f"Room {room_number} has been updated to {room}")
        else:
            print(f"Room {room_number} not found.")

    def search_by_room_type(self, room_type):
        available_rooms = [room for room in self.rooms if room.room_type == room_type and not room.is_booked]
        if not available_rooms:
            print(f"No available rooms of type {room_type}.")
        else:
            for room in available_rooms:
                print(room)


def main():
    hotel = Hotel()

    while True:
        print("\n1. Add Room")
        print("\n2. Check Room Availability")
        print("\n3. Book Room")
        print("\n4. Cancel Booking")
        print("\n5. Modify Room")
        print("\n6. Search Available Rooms by Type")
        print("\n7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            room_number = input("Enter room number: ")
            room_type = input("Enter room type (e.g., Single, Double, Suite): ")
            price = float(input("Enter room price: "))
            hotel.add_room(room_number, room_type, price)
        elif choice == '2':
            hotel.check_availability()
        elif choice == '3':
            room_number = input("Enter room number to book: ")
            hotel.book_room(room_number)
        elif choice == '4':
            room_number = input("Enter room number to cancel booking: ")
            hotel.cancel_booking(room_number)
        elif choice == '5':
            room_number = input("Enter room number to modify: ")
            new_room_type = input("Enter new room type (leave blank to keep current): ")
            new_price = input("Enter new room price (leave blank to keep current): ")
            new_price = float(new_price) if new_price else None
            hotel.modify_room(room_number, new_room_type, new_price)
        elif choice == '6':
            room_type = input("Enter room type to search for: ")
            hotel.search_by_room_type(room_type)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
