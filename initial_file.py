# Person A - Dilyan Savov
# D00290447
# CA1 Object-Oriented Programming
# Classes for event and venue
# this is from my initial file from my initial repository

# Creating a class event
class Ev///ent:
    # creating a list of possible event types
    _event_type = ["workshop", "open day", "conference", "convention"]
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
# Creating a class venue
class Ve///nue:
    # creating preset variables for the venue
    venue_id = ''
    venue_name = ''
    venue_capacity = 1000
    # calling to the variables
    def __init__(self, venue_id, venue_name, venue_capacity):
        self.venue_id = venue_id
        self.venue_name = venue_name
        self.venue_capacity = venue_capacity