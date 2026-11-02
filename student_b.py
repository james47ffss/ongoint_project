# Person B - Adam Gorman Devlin
# D00294545
# CA1 Object-Oriented Programming
# Classes for Attendee and Booking

class Attendee: #creates a class called Attendee

    # function for defining the class
    def __init__(self, attendee_id: int, name: str, email: str):

        # Creates an attendee with a valid ID, name and email.

        if self.is_valid_email(email):
            self.email = email
        else:
            self.email = "Invalid"

        # saves the info inside the object
        self.attendee_id = attendee_id
        self.name = name

    # function for checking if the email is valid
    def is_valid_email(self, email: str) -> bool:

        # Checks whether an email address has a basic valid format.

        parts = email.split("@") # splits the email into 2 parts before and after the @

        if len(parts) != 2: # makes sure there are only 2 parts in the email
            return False

        if parts[0] == "": # checks if the first part is empty
            return False

        if parts[1] == "": # checks if the second part is empty
            return False

        if "." not in parts[1]: # checks that there is a . in the second part
            return False

        email_parts = parts[1].split(".") # splits the email into 2 parts before and after the .

        if email_parts[0] == "": # checks if before the . is empty
            return False

        if email_parts[-1] == "": # checks if after the . is empty
            return False

        return True # if the email passes returns it as passed

    # function for changing the email address of an existing attendee
    def update_email(self, new_email: str) -> bool:

        # Updates the email if the new address is valid.

        # calls the validation function and validates the new email
        if self.is_valid_email(new_email):
            self.email = new_email # sets the email as the new email
            return True # if valid replace email

        return False # if not valid dont replace

    # function to display the attendee
    def __str__(self) -> str:

        # Returns readable attendee information.

        return (
            f"Attendee ID: {self.attendee_id}, "
            f"Name: {self.name}, "
            f"Email: {self.email}"
        )

if __name__ == "__main__":
    #test
    attendee1 = Attendee(47, "John Smith", "john@gmail.com")
    print(attendee1)
    attendee2 = Attendee(74,"Dave Davidson", "dave@yahoo.com")
    print(attendee2)
    attendee3 = Attendee(26,"David Free", "free@.com")
    print(attendee3)
    attendee4 = Attendee(64,"Mark Davids", "mark@")
    print(attendee4)
    attendee5 = Attendee(35,"David Dee", "dee.com")
    print(attendee5)
    attendee6 = Attendee(16,"Jess Tully", "Jess@gmail")
    print(attendee6)

# Imports the Event class from Student A's event.py file
from student_a import Event

# Imports the date type from Python's datetime library
from datetime import date

class Booking: # creates a class called Booking

    # function for defining the class
    def __init__(
        self,
        booking_id: int,
        attendee: Attendee,
        event: Event,
        booking_date: date
    ):

        # Creates a new booking using an ID, attendee, event and booking date.

        # Checks that an attendee has been provided
        if attendee is None:
            raise ValueError("Attendee cannot be None")

        # Checks that an event has been provided
        if event is None:
            raise ValueError("Event cannot be None")

        # Saves the booking information inside the object
        self.booking_id = booking_id
        self.attendee = attendee
        self.event = event
        self.booking_date = booking_date

        # Sets the booking status to not canceled when first created
        self.cancelled = False

    # function for changing the attendee associated with a booking
    def change_attendee(self, new_attendee: Attendee) -> bool:

        # Checks whether a new attendee has been provided
        if new_attendee is None:
            return False

        # Checks that the new attendee is an Attendee object
        if not isinstance(new_attendee, Attendee):
            return False

        # Replaces the current attendee with the new attendee
        self.attendee = new_attendee

        return True # returns True if the attendee was successfully changed

    # function for cancelling a booking
    def cancel(self) -> None:

        # Changes the booking status to canceled
        self.cancelled = True

    # function for displaying the booking information
    def __str__(self) -> str:

        # Checks whether the booking is canceled or active
        status = "Cancelled" if self.cancelled else "Active"

        # Returns the booking information in a readable format
        return (
            f"Booking ID: {self.booking_id}, "
            f"Attendee: {self.attendee.name}, "
            f"Event: {self.event.title}, "
            f"Date: {self.booking_date}, "
            f"Status: {status}"
        )
