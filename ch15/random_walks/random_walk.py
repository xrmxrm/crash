from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            x_step = self.get_step([0, 1, 2, 3, 4])
            y_step = self.get_step([0, 1, 2, 3, 4])

            # If it's a real move, add it.
            if x_step or y_step:
                # Calculate the new position.
                x = self.x_values[-1] + x_step
                y = self.y_values[-1] + y_step
                self.x_values.append(x)
                self.y_values.append(y)

    def get_step(self, lengths, factor=1):
        direction = choice([factor, -factor])
        return direction * choice(lengths)    
