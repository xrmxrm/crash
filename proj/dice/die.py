from random import randint

class Die:
    """Represent a single die of the specified number of sides"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"** {randint(1,self.sides)} **")