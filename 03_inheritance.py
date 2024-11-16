class Animal:
    """
    This class demonstrates the concept of inheritance in OOP.

    The Animal class is a base class that represents generic animals. It has a method 
    `speak` that can be overridden by subclasses to provide specific behavior for different animals.
    """

    def __init__(self, name):
        """
        Initialize the Animal object with a name.

        Args:
            name (str): The name of the animal.
        """
        self.name = name  # Assign the name of the animal

    def speak(self):
        """
        Represent a generic animal sound.

        Returns:
            None: Prints a generic message that the animal makes a sound.
        """
        print(f"{self.name} makes a sound")  # Default sound for animals


class Dog(Animal):
    """
    This class demonstrates method overriding in OOP.

    The Dog class inherits from the Animal class and overrides the `speak` method 
    to represent a dog-specific behavior (barking).
    """

    def speak(self):
        """
        Override the `speak` method to make the dog bark.

        Returns:
            None: Prints a message that the dog barks.
        """
        print(f"{self.name} barks")  # Override speak method to make the dog bark


# Create an object of the Dog class
dog = Dog("Buddy")

# Calling the overridden speak method for the Dog object
dog.speak()  # Expected output: "Buddy barks"
