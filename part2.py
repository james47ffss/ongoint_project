from student_a import Venue
from student_a import Event
from student_b import Attendee
from student_b import Booking

if __name__ == "__main__":
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
    booking1 = Booking(1, attendees[0], event[0], date(2026, 12, 10, time(10, 0)))
    booking2 = Booking(2, attendees[1], event[1], date(2026, 12, 15, time(11, 0)))
    booking3 = Booking(3, attendees[2], events[2], date(2027, 1, 20, time(9, 30)))
    booking4 = Booking(4, attendees[0], events[3], date(2027, 2, 5, time(12, 0)))
    booking5 = Booking(5, attendees[1], events[4], date(2027, 2, 15, time(14, 0)))

    # adding bookings to list
    bookings.append(booking1)
    bookings.append(booking2)
    bookings.append(booking3)
    bookings.append(booking4)
    bookings.append(booking5)
    