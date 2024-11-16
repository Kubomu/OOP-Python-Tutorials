class Point:
    """
    A class representing a point in a 2D space.

    This class provides the ability to represent a point with x and y coordinates.
    It also overrides the __str__ and __add__ methods to allow for custom string representation
    and the addition of two Point objects, respectively.
    """

    def __init__(self, x, y):
        """
        Initialize a Point object with x and y coordinates.

        Args:
            x (int or float): The x-coordinate of the point.
            y (int or float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a string representation of the Point object.

        This method is called when using the `print()` function or `str()` on a Point object.

        Returns:
            str: A formatted string representing the point, e.g., "Point(2, 3)".
        """
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        """
        Overload the addition operator to add two Point objects.

        This method defines how to add two Point objects by adding their respective x and y coordinates.

        Args:
            other (Point): Another Point object to add.

        Returns:
            Point: A new Point object that is the result of adding the two points.
        """
        return Point(self.x + other.x, self.y + other.y)


# Create two Point objects
point1 = Point(2, 3)
point2 = Point(5, 7)

# Print the result of adding the two points
print(point1 + point2)  # Expected output: Point(7, 10)
