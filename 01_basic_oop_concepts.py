# Defining the Car class
class Car:
    """
    1. Basic Concepts of OOP:
    
    Classes and Objects:
    - A class is a blueprint for creating objects (a particular data structure), 
      providing initial values for state (member variables or properties), 
      and implementations of behavior (member functions or methods).
    - An object is an instance of a class.

    Attributes:
        make (str): The make of the car (e.g., Toyota, Honda).
        model (str): The model of the car (e.g., Corolla, Civic).
        year (int): The year of manufacture for the car.

    Methods:
        display_info(): Prints the car's year, make, and model.
    """

    # Constructor method to initialize the Car object with make, model, and year
    def __init__(self, make, model, year):
        """
        Initialize the car object with make, model, and year.

        Args:
            make (str): The make of the car (e.g., Toyota, Honda).
            model (str): The model of the car (e.g., Corolla, Civic).
            year (int): The year the car was manufactured.
        """
        # Initializing the instance variables (attributes) for the car
        self.make = make  # The make of the car (e.g., Toyota, Honda)
        self.model = model  # The model of the car (e.g., Corolla, Civic)
        self.year = year  # The year of manufacture for the car

    # Method to display the car's information
    def display_info(self):
        """
        Prints the car's year, make, and model in a formatted string.
        """
        # Prints out the car's year, make, and model in a formatted string
        print(f"{self.year} {self.make} {self.model}")

# Creating two objects (instances) of the Car class
car1 = Car("Toyota", "Corolla", 2020)  # Creating a Toyota Corolla from 2020
car2 = Car("Honda", "Civic", 2021)  # Creating a Honda Civic from 2021

# Calling the display_info method on car1 object to print its information
car1.display_info()  # Expected output: "2020 Toyota Corolla"

# Calling the display_info method on car2 object to print its information
car2.display_info()  # Expected output: "2021 Honda Civic"
