class Restaurant:
    """Represents a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

class IceCreamStand(Restaurant):

    """Represents an ice-cream stand"""

    def __init__(self, name, flavors):
        super().__init__(name, 'ice cream')
        self.flavors = flavors

    def show_flavors(self):
        print("Flavors:  ", end=' ')
        for flavor in self.flavors:
            print(f"{flavor}  ", end=' ')
