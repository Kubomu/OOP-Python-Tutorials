"""
Autograder for practice.py.

You do not need to edit this file. It is what `python check.py`, `pytest`, and
the green check on GitHub all run to confirm your solutions are correct.
"""

import math

import pytest

import practice as p


# 1. Classes and Objects -----------------------------------------------------
def test_person_introduce():
    assert p.Person("Ada", 36).introduce() == "Hi, I'm Ada and I'm 36 years old."


def test_person_is_adult():
    assert p.Person("Ada", 36).is_adult() is True
    assert p.Person("Sam", 12).is_adult() is False


# 2. Encapsulation -----------------------------------------------------------
def test_bankaccount_deposit_and_withdraw():
    acc = p.BankAccount()
    acc.deposit(100)
    acc.withdraw(30)
    assert acc.get_balance() == 70


def test_bankaccount_ignores_invalid_amounts():
    acc = p.BankAccount(50)
    acc.deposit(-10)
    acc.deposit(0)
    acc.withdraw(1000)
    assert acc.get_balance() == 50


def test_bankaccount_balance_is_private():
    acc = p.BankAccount(40)
    # the balance must live in __balance (name-mangled), not a public attribute
    assert not hasattr(acc, "balance")


# 3. Inheritance -------------------------------------------------------------
def test_inheritance_overrides_start():
    assert p.Car("Toyota", "Corolla", 2020).start() == "Car engine starting..."
    assert p.Motorcycle("Yamaha", "MT", 2021).start() == "Motorcycle engine revving..."


def test_inheritance_keeps_base_attributes():
    car = p.Car("Toyota", "Corolla", 2020)
    assert car.brand == "Toyota"
    assert car.year == 2020


# 4. Polymorphism ------------------------------------------------------------
def test_polymorphism_areas():
    assert p.Rectangle(3, 4).calculate_area() == 12
    assert math.isclose(p.Circle(2).calculate_area(), math.pi * 4)


def test_polymorphism_total_area():
    shapes = [p.Rectangle(2, 2), p.Circle(1)]
    assert math.isclose(p.total_area(shapes), 4 + math.pi)


# 5. Abstraction -------------------------------------------------------------
def test_abstract_animal_cannot_be_created():
    with pytest.raises(TypeError):
        p.Animal()


def test_abstract_children_implement_methods():
    assert p.Cat().make_sound() == "Meow"
    assert p.Cat().move() == "Cat walks on four legs"
    assert p.Fish().make_sound() == "Bubble"
    assert p.Fish().move() == "Fish swims in water"


# 6. Magic methods -----------------------------------------------------------
def test_vector_str():
    assert str(p.Vector(1, 2)) == "Vector(1, 2)"


def test_vector_add():
    assert p.Vector(1, 2) + p.Vector(3, 4) == p.Vector(4, 6)


def test_vector_equality():
    assert p.Vector(1, 2) == p.Vector(1, 2)
    assert p.Vector(1, 2) != p.Vector(9, 9)
