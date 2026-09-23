
print("==============================")
print("     MOVIE TICKET BOOKING")
print("==============================")

movies = {
    "1": {
        "name": "Avengers",
        "price": 300,
        "seats": ["A1", "A2", "A3", "A4", "A5"]
    },
    "2": {
        "name": "Interstellar",
        "price": 350,
        "seats": ["B1", "B2", "B3", "B4", "B5"]
    },
    "3": {
        "name": "Inception",
        "price": 320,
        "seats": ["C1", "C2", "C3", "C4", "C5"]
    }
}

bookings = []


def show_movies():
    print("\n========== MOVIES ==========")

    for movie_id, movie in movies.items():
        print(f"{movie_id}. {movie['name']} - Rs.{movie['price']}")


def show_seats(movie):
    print("\nAvailable Seats:")

    if movie["seats"]:
        print(", ".join(movie["seats"]))
    else:
        print("No seats available.")


def book_ticket():
    show_movies()

    movie_id = input("\nEnter movie number: ")

    if movie_id not in movies:
        print("Invalid movie selection.")
        return

    movie = movies[movie_id]

    show_seats(movie)

    if not movie["seats"]:
        return

    seat = input("Enter seat number: ").upper()

    if seat not in movie["seats"]:
        print("Invalid or already booked seat.")
        return

    name = input("Enter your name: ")

    movie["seats"].remove(seat)

    booking = {
        "name": name,
        "movie": movie["name"],
        "seat": seat,
        "price": movie["price"]
    }

    bookings.append(booking)

    print("\nTicket booked successfully!")
    print(f"Customer: {name}")
    print(f"Movie: {movie['name']}")
    print(f"Seat: {seat}")
    print(f"Price: Rs.{movie['price']}")


def cancel_booking():
    if not bookings:
        print("\nNo bookings found.")
        return

    name = input("\nEnter customer name: ")

    found = False

    for booking in bookings:
        if booking["name"].lower() == name.lower():

            for movie_id, movie in movies.items():
                if movie["name"] == booking["movie"]:
                    movie["seats"].append(booking["seat"])
                    movie["seats"].sort()

            bookings.remove(booking)

            print("Booking cancelled successfully.")
            found = True
            break

    if not found:
        print("Booking not found.")


def search_booking():
    if not bookings:
        print("\nNo bookings found.")
        return

    name = input("\nEnter customer name: ")

    found = False

    for booking in bookings:
        if booking["name"].lower() == name.lower():

            print("\n========== BOOKING ==========")
            print(f"Customer : {booking['name']}")
            print(f"Movie    : {booking['movie']}")
            print(f"Seat     : {booking['seat']}")
            print(f"Price    : Rs.{booking['price']}")

            found = True

    if not found:
        print("Booking not found.")


def show_bookings():
    if not bookings:
        print("\nNo bookings found.")
        return

    print("\n========== ALL BOOKINGS ==========")

    for number, booking in enumerate(bookings, start=1):
        print(f"\nBooking {number}")
        print(f"Customer : {booking['name']}")
        print(f"Movie    : {booking['movie']}")
        print(f"Seat     : {booking['seat']}")
        print(f"Price    : Rs.{booking['price']}")


def total_sales():
    total = 0

    for booking in bookings:
        total += booking["price"]

    print(f"\nTotal Sales: Rs.{total}")


while True:

    print("\n==============================")
    print("     MOVIE TICKET BOOKING")
    print("==============================")
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. Cancel Booking")
    print("4. Search Booking")
    print("5. Show All Bookings")
    print("6. Show Total Sales")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_movies()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        cancel_booking()

    elif choice == "4":
        search_booking()

    elif choice == "5":
        show_bookings()

    elif choice == "6":
        total_sales()

    elif choice == "7":
        print("\nThank you for using Movie Ticket Booking System!")
        break

    else:
        print("Invalid choice. Please try again.")
