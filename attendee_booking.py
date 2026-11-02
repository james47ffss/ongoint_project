# list for storing the attendees
attendees= []

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
booking1 = booking(1, attendees[0], event[0], date())
booking2 = booking(2, attendees[1], event[1], date())
booking3 = Booking(3, attendees[2], events[2], date())
booking4 = Booking(4, attendees[0], events[3], date())
booking5 = Booking(5, attendees[1], events[4], date())

# adding bookings to list
bookings.append(booking1)
bookings.append(booking2)
bookings.append(booking3)
bookings.append(booking4)
bookings.append(booking5)
