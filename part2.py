from student_a import Venue
from student_a import Event
from student_b import Attendee
from student_b import Booking

from datetime import date as date_type, time

if __name__ == "__main__":
    # Student A - Dilyan Savov
    # D00290447
    # CA1 Object-Oriented Programming
    # Events and Venues PART 2

    # Storing the venues in a list
    venues = []

    # Creating venue1, venue2 and venue3 objects
    # Appending each of the venues to their respective list
    venue1 = Venue(1, "Dundalk Park", 200)
    venues.append(venue1)
    venue2 = Venue(2, "PJ Carrols Building", 800)
    venues.append(venue2)
    venue3 = Venue(3, "Gateway Hotel", 320)
    venues.append(venue3)

    # Storing the events in a list
    events = []

    # Adding 5 event objects
    # Appending each of the events to their respective list
    events1 = Event("workshop", 1, "Python Workshop", date_type(2026, 12, 10), time(10, 0), 50, venue1, True, 15.00)
    events.append(events1)
    events2 = Event("open day", 2, "DKiT Open Day", date_type(2026, 12, 15), time(11, 0), 150, venue2, False, 0.00)
    events.append(events2)
    events3 = Event("conference", 3, "Technology Conference", date_type(2027, 1, 20), time(9, 30), 300, venue2, False,25.00)
    events.append(events3)
    event4 = Event("convention", 4, "Coding convention", date_type(2027, 2, 5), time(12, 0), 90, venue3, True, 20.00)
    events.append(event4)
    event5 = Event("workshop", 5, "Science convention", date_type(2027, 2, 15), time(14, 0), 40, venue1, False, 10.00)
    events.append(event5)

    # Header for all events
    print("All events:")
    for event in events:
        print(event)

    # Header for all venues
    print("All venues:")
    for venue in venues:
        print(venue)

    # Header for active events
    print("Active events")
    for event in events:
        if not event.cancelled:
            print(event)
#------------------------------------------------------
    # Person A - Adam Gorman Devlin
    # D00294545
    # CA1 Object-Oriented Programming
    # Classes for Attendee and Booking

    # list for storing the attendees
    attendees = []

    # attendees
    attendee1 = Attendee(1, "John smith", "john@gmail.com")
    attendee2 = Attendee(2, "Jess davidson", "jess@gyahoo.com")
    attendee3 = Attendee(3, "Timmy turner", "tim@hotmail.com")

    # adding attendees to list
    attendees.append(attendee1)
    attendees.append(attendee2)
    attendees.append(attendee3)

    # list for storing the bookings
    bookings = []

    # bookings
    booking1 = Booking(1, attendees[0], events[0], date_type(2026, 12, 10))
    booking2 = Booking(2, attendees[1], events[1], date_type(2026, 12, 15))
    booking3 = Booking(3, attendees[2], events[2], date_type(2027, 1, 20))
    booking4 = Booking(4, attendees[0], events[3], date_type(2027, 2, 5))
    booking5 = Booking(5, attendees[1], events[4], date_type(2027, 2, 15))

    # adding bookings to list
    bookings.append(booking1)
    bookings.append(booking2)
    bookings.append(booking3)
    bookings.append(booking4)
    bookings.append(booking5)

    # cancelling a booking if a booking is cancelled
    for booking in bookings:
        if booking.event.cancelled:
            booking.cancelled = True
        else:
            booking.cancelled = False

    # displaying all attendees
    print("All attendees")
    for attendee in attendees:
        print(attendee)

    # displaying all bookings
    print("All bookings")
    for booking in bookings:
        print(booking)

    # displaying all active bookings
    print("Active bookings")
    for booking in bookings:
        if not booking.cancelled:
            print(booking)

    # display all canceled booking
    print("Cancelled Bookings")

    for booking in bookings:
        if booking.cancelled == True:
            print(booking)

    #  Find and display all bookings for a specific Attendee
    print("Specific attendee")
    specific_attendee = attendees[0]
    for booking in bookings:
        if booking.attendee == specific_attendee:
            print(booking)