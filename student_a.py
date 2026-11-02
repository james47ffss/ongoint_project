# Person A - Dilyan Savov
# D00290447
# CA1 Object-Oriented Programming
# Classes for event and venue

# Importing date times
from datetime import date as date_type, time, datetime

# Creating a class event
class Event:
    # creating a list of possible event types
    _event_types = ["workshop", "open day", "conference", "convention"]
    # create a personalised body for each of the event venues with their capacity, if user input is greater than, then it gives out an error message saying there is too much

    # creating a function for the class to call to the variables
    def __init__(self, _event_type, title, date, start_time, capacity, venue, cancelled, ticket_price):
        self._event_type = _event_type
        self.title = title
        self.date = date
        self.start_time = start_time
        self.capacity = capacity
        self.venue = venue
        self.cancelled = cancelled
        self.ticket_price = ticket_price

        # using a while loop so if a user enters wrong event, it will just break
        while _event_type not in self._event_types:
            print("invalid event type")
            break

        # checking if the date and time are correct
        while not isinstance(date, date_type) or not isinstance(start_time, time):
            print("invalid date or time")
            break

        # checking if capacity is positive
        while capacity <= 0:
            print("invalid capacity")
            break

        # checking if venue has enough capacity
        while not isinstance(venue, Venue) or capacity > venue.venue.capacity:
            print("invalid capacity")
            break

        # checking ticket prices if it's less than 0
        while ticket_price < 0:
            print("invalid ticket price")
            break

    # creating a function to update date and start time
    def update_schedule(self, new_date, new_time):
        # checking if new time and date are correct
        if isinstance(new_date, date_type) and isinstance(new_time, time):
            self.date = new_date
            self.start_time = new_time
            return True
        return False

    def change_venue(self, new_venue):
        if isinstance(new_venue, Venue) and new_venue.venue_capacity >= self._capacity:
            self.venue = new_venue
            return True
        return False

# Creating a class venue
class Venue:
    # creating preset variables for the venue
    venue_id = ''
    venue_name = ''
    venue_capacity = 1000
    # calling to the variables
    def __init__(self, venue_id, venue_name, venue_capacity):
        self.venue_id = venue_id
        self.venue_name = venue_name
        self.venue_capacity = venue_capacity
