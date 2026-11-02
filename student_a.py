# Student A - Dilyan Savov
# D00290447
# CA1 Object-Oriented Programming
# Classes for event and venue

# Importing date times
from datetime import date as date_type, time, datetime

# Creating a class event
class Event:
    # creating a list of possible event types
    _event_types = ["workshop", "open day", "conference", "convention"]

    # creating a function for the class to call to the variables
    def __init__(self, _event_type, _event_id, title, date, start_time, capacity, venue, cancelled, ticket_price):
        self._event_type = _event_type
        self._event_id = _event_id
        self.title = title
        self.date = date
        self.start_time = start_time
        self._capacity = capacity
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
        while not isinstance(venue, Venue) or capacity > venue.venue_capacity:
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
    # function for changing the venue
    def change_venue(self, new_venue):
        if isinstance(new_venue, Venue) and new_venue.venue_capacity >= self._capacity:
            self.venue = new_venue
            return True
        return False

    # creating a function to change event type
    def change_type(self, new_type):
        if new_type in self._event_types:
            self._event_type = new_type
            return True
        return False

    # a function to cancel the event
    def cancel_event(self):
        event_start = datetime.combine(self.date, self.start_time)
        if event_start > datetime.now() and not self.cancelled:
            self.cancelled = True
            return True
        return False

    # a function to show event information
    def __str__(self):
        # returns all values in a neat format
        return (f"Event ID: {self._event_id}, Title: {self.title} "
                f"Type: {self._event_type}, Date: {self.date} "
                f"Start Time: {self.start_time}, Capacity: {self._capacity} "
                f"Venue: {self.venue}, Cancelled: {self.cancelled} "
                f"Ticket Price: {self.ticket_price} ")

# Creating a class venue
class Venue:
    # calling to the variables
    def __init__(self, venue_id, venue_name, venue_capacity):
        self.venue_id = venue_id
        self.venue_name = venue_name
        self.venue_capacity = venue_capacity

        # checking if venue capacity is positive
        while venue_capacity <= 0:
            print("invalid capacity")
            break
    # a function for desplaying the venue information
    def __str__(self):
        return (f"Venue ID: {self.venue_id}"
                f"Name: {self.venue_name}"
                f"Capacity: {self.venue_capacity}")