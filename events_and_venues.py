# Student A - Dilyan Savov
# D00290447
# CA1 Object-Oriented Programming
# Events and Venues PART 2

# importing Event and Venue classes from file student_a
from student_a import Event, Venue

# importing date and time
from datetime import date as date_type, time

# storing the venues in a list
venues = []

# creating venue1, venue2 and venue3 objects
# Appending each of the venues to their respective list
venue1 = Venue(1, "Dundalk Park")
venues.append(venue1)
venue2 = Venue(2, "PJ Carrols Building")
venues.append(venue2)
venue3 = Venue(3, "Gateway Hotel")
venues.append(venue3)


# storing the events in a list
events = []

# adding 5 event objects
# Appending each of the events to their respective list
events1 = Event("workshop", 1, "Python Workshop",date_type(2026, 12, 10), time(10, 0), 50, venue1, False, 15.00)
events.append(events1)
events2 = Event("open day", 2, "DKiT Open Day", date_type(2026, 12, 15), time(11, 0), 150, venue2, False, 0.00)
events.append(events2)
events3 = Event("conference", 3, "Technology Conference", date_type(2027, 1, 20), time(9, 30), 300, venue2, False, 25.00)
events.append(events3)
event4 = Event("convention", 4, "Coding convention", date_type(2027, 2, 5), time(12, 0), 90, venue3, False, 20.00)
events.append(event4)
event5 = Event("workshop", 5, "Science convention", date_type (2027, 2, 15), time(14, 0), 40, venue1, False, 10.00)
events.append(event5)

# header for all events
print("All events:")
for event in events:
    print(events)

# header for all venues
print("All venues:")
for venue in venues:
    print(venues)

