class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

class Privileges:
    """Represents a set of privileges"""

    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print(self.privileges)

class Admin(User):

   def __init__(self, first_name, last_name, username, email, location, privileges):
      super().__init__(first_name, last_name, username, email, location)
      self.privileges = privileges
