"""
Practice exercises for the OOP in Python tutorial.

HOW THIS WORKS
  1. Every class below has a `# TODO` and raises NotImplementedError.
  2. Replace each TODO with your own code so the behaviour matches the docstring.
  3. Check your work instantly. From the repo folder run either:
         python check.py     (friendly scoreboard, one line per topic)
         pytest              (full detail on what passed and failed)
  4. A topic turns green once its tests pass. Keep going until all six pass.

Stuck on one? Open the matching lesson file (01_ through 06_) for a worked
example, then come back and try again. You cannot break anything here.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# 1. Classes and Objects            (worked example: 01_basic_oop_concepts.py)
# ---------------------------------------------------------------------------
class Person:
    """A person with a name and an age.

    >>> Person("Ada", 36).introduce()
    "Hi, I'm Ada and I'm 36 years old."
    >>> Person("Ada", 36).is_adult()
    True
    >>> Person("Sam", 12).is_adult()
    False
    """

    def __init__(self, name, age):
        # TODO: save name and age on the instance (self.name = name, etc.)
        raise NotImplementedError("Exercise 1: fill in Person.__init__")

    def introduce(self):
        # TODO: return the sentence shown in the docstring above
        raise NotImplementedError("Exercise 1: fill in Person.introduce")

    def is_adult(self):
        # TODO: return True when age is 18 or more, otherwise False
        raise NotImplementedError("Exercise 1: fill in Person.is_adult")


# ---------------------------------------------------------------------------
# 2. Encapsulation                  (worked example: 02_encapsulation.py)
# ---------------------------------------------------------------------------
class BankAccount:
    """A bank account that protects its balance behind methods.

    >>> acc = BankAccount()
    >>> acc.deposit(100)
    >>> acc.withdraw(30)
    >>> acc.get_balance()
    70

    Rules:
      - deposit ignores amounts that are zero or negative
      - withdraw ignores amounts that are zero, negative, or more than the balance
    """

    def __init__(self, starting_balance=0):
        # TODO: keep the money in a PRIVATE attribute named __balance
        raise NotImplementedError("Exercise 2: fill in BankAccount.__init__")

    def deposit(self, amount):
        # TODO: add amount to the balance only when amount is greater than 0
        raise NotImplementedError("Exercise 2: fill in BankAccount.deposit")

    def withdraw(self, amount):
        # TODO: subtract amount only when 0 < amount <= current balance
        raise NotImplementedError("Exercise 2: fill in BankAccount.withdraw")

    def get_balance(self):
        # TODO: return the current balance
        raise NotImplementedError("Exercise 2: fill in BankAccount.get_balance")


# ---------------------------------------------------------------------------
# 3. Inheritance                    (worked example: 03_inheritance.py)
# ---------------------------------------------------------------------------
class Vehicle:
    """Base vehicle. This one is finished for you, use it as a reference."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        return "Vehicle starting..."


class Car(Vehicle):
    def start(self):
        # TODO: return "Car engine starting..." instead of the base message
        raise NotImplementedError("Exercise 3: override Car.start")


class Motorcycle(Vehicle):
    def start(self):
        # TODO: return "Motorcycle engine revving..."
        raise NotImplementedError("Exercise 3: override Motorcycle.start")


# ---------------------------------------------------------------------------
# 4. Polymorphism                   (worked example: 04_polymorphism.py)
# ---------------------------------------------------------------------------
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        # TODO: return width times height
        raise NotImplementedError("Exercise 4: fill in Rectangle.calculate_area")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        # TODO: return pi times radius squared (use math.pi)
        raise NotImplementedError("Exercise 4: fill in Circle.calculate_area")


def total_area(shapes):
    """Return the summed area of any list of shapes that have calculate_area().

    This is polymorphism: the function does not care whether a shape is a
    Rectangle or a Circle, only that it knows how to calculate its own area.
    """
    # TODO: add up calculate_area() for every shape in the list and return it
    raise NotImplementedError("Exercise 4: fill in total_area")


# ---------------------------------------------------------------------------
# 5. Abstraction                    (worked example: 05_abstraction.py)
# ---------------------------------------------------------------------------
class Animal(ABC):
    """Abstract animal. You cannot create an Animal directly, only its children.
    This one is finished for you."""

    @abstractmethod
    def make_sound(self):
        ...

    @abstractmethod
    def move(self):
        ...


class Cat(Animal):
    # TODO: implement make_sound to return "Meow"
    # TODO: implement move to return "Cat walks on four legs"
    pass


class Fish(Animal):
    # TODO: implement make_sound to return "Bubble"
    # TODO: implement move to return "Fish swims in water"
    pass


# ---------------------------------------------------------------------------
# 6. Magic methods                  (worked example: 06_magic_methods.py)
# ---------------------------------------------------------------------------
class Vector:
    """A 2D vector that supports printing, addition, and equality.

    >>> str(Vector(1, 2))
    'Vector(1, 2)'
    >>> Vector(1, 2) + Vector(3, 4) == Vector(4, 6)
    True
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # TODO: return the text "Vector(x, y)" using this vector's x and y
        raise NotImplementedError("Exercise 6: fill in Vector.__str__")

    def __add__(self, other):
        # TODO: return a new Vector whose x and y are the two vectors added
        raise NotImplementedError("Exercise 6: fill in Vector.__add__")

    def __eq__(self, other):
        # TODO: return True when both x and y match the other vector
        raise NotImplementedError("Exercise 6: fill in Vector.__eq__")
