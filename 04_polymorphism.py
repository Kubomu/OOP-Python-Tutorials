class Bird:
    """
    This class demonstrates polymorphism in OOP with a fly method.

    The Bird class defines the behavior of a bird. It has a method `fly` 
    that prints the message indicating that a bird can fly.
    """
    
    def fly(self):
        """
        Method to represent a bird flying.
        
        Returns:
            None: Prints a message that the bird can fly.
        """
        print("Bird can fly")


class Airplane:
    """
    This class demonstrates polymorphism in OOP with a fly method.

    The Airplane class defines the behavior of an airplane. It has a method `fly` 
    that prints the message indicating that an airplane can fly.
    """

    def fly(self):
        """
        Method to represent an airplane flying.
        
        Returns:
            None: Prints a message that the airplane can fly.
        """
        print("Airplane can fly")


# Using polymorphism to make different objects perform the same action (fly)
def make_it_fly(flyable_object):
    """
    This function demonstrates polymorphism by calling the `fly` method
    on any object that has a `fly` method.

    Args:
        flyable_object (object): An object that has a `fly` method.
    """
    flyable_object.fly()  # Calls the fly method of the passed object


# Creating instances of Bird and Airplane
bird = Bird()
airplane = Airplane()

# Using polymorphism to call the fly method on both objects
make_it_fly(bird)  # Expected output: "Bird can fly"
make_it_fly(airplane)  # Expected output: "Airplane can fly"
