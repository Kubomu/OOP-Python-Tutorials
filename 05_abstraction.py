from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract class that defines a blueprint for shapes.

    This class uses the `abstractmethod` decorator to enforce that any subclass 
    must implement the `area` method. The `Shape` class cannot be instantiated 
    directly, but provides a common interface for different shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method that must be implemented by any subclass.

        This method will calculate and return the area of the shape.
        
        Returns:
            float: The area of the shape.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle, a type of shape.

    The Circle class implements the abstract `area` method from the Shape class 
    and calculates the area of the circle based on its radius.
    """

    def __init__(self, radius):
        """
        Initialize the Circle object with a radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Uses the formula: Area = π * radius^2

        Returns:
            float: The area of the circle.
        """
        return 3.14 * self.radius * self.radius


# Create an instance of Circle
circle = Circle(5)

# Print the area of the circle
print(f"Area of circle: {circle.area()}")
