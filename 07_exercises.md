# OOP Practice Exercises

Test your understanding of Object-Oriented Programming in Python with these exercises! Try to complete them on your own before looking at the tutorial files for help.

---

## 1. Classes and Objects

### Exercise 1.1: Create a Person class
Create a class called `Person` with the following:
- Attributes: `name` (string) and `age` (integer)
- Method: `introduce()` that prints "Hi, I'm [name] and I'm [age] years old."

**Bonus:** Add a method `is_adult()` that returns `True` if age >= 18, otherwise `False`.

### Exercise 1.2: Create a Book class
Create a class called `Book` with:
- Attributes: `title`, `author`, and `pages`
- Method: `description()` that prints the book's details
- Method: `is_long()` that returns `True` if the book has more than 300 pages

---

## 2. Encapsulation

### Exercise 2.1: Create a BankAccount class
Create a class called `BankAccount` that:
- Has a private attribute `__balance` (initialized to 0 or a given amount)
- Method: `deposit(amount)` - adds money to the balance (only positive amounts)
- Method: `withdraw(amount)` - removes money (only if sufficient balance exists)
- Method: `get_balance()` - returns the current balance
- The balance should NOT be directly accessible from outside the class

### Exercise 2.2: Create a Password class
Create a class called `Password` that:
- Has a private attribute `__password`
- Method: `set_password(new_password)` - sets the password (minimum 8 characters)
- Method: `check_password(attempt)` - returns `True` if attempt matches the password
- The actual password should never be directly accessible

**Bonus:** Add password strength validation (must contain at least one number and one uppercase letter).

---

## 3. Inheritance

### Exercise 3.1: Create a Vehicle hierarchy
Create a base class `Vehicle` with:
- Attributes: `brand`, `model`, `year`
- Method: `start()` that prints "Vehicle starting..."

Then create two child classes:
- `Car(Vehicle)` - override `start()` to print "Car engine starting..."
- `Motorcycle(Vehicle)` - override `start()` to print "Motorcycle engine revving..."

### Exercise 3.2: Create an Employee hierarchy
Create a base class `Employee` with:
- Attributes: `name`, `employee_id`, `base_salary`
- Method: `get_salary()` that returns the base salary

Create two child classes:
- `Manager(Employee)` - add attribute `bonus` and override `get_salary()` to include bonus
- `Developer(Employee)` - add attribute `programming_language` and a method `code()` that prints what language they're coding in

---

## 4. Polymorphism

### Exercise 4.1: Create different payment methods
Create three classes: `CreditCard`, `PayPal`, and `Cash`, each with:
- A method `pay(amount)` that prints how the payment was made

Then create a function `process_payment(payment_method, amount)` that accepts any payment object and calls its `pay()` method.

### Exercise 4.2: Create different shapes
Create classes `Rectangle`, `Triangle`, and `Circle`, each with:
- A method `calculate_area()` that returns the area of the shape

Create a function `print_area(shape)` that works with any shape object and prints its area.

**Hint:**
- Rectangle area = length × width
- Triangle area = 0.5 × base × height
- Circle area = π × radius²

---

## 5. Abstraction

### Exercise 5.1: Create an abstract Animal class
Create an abstract base class `Animal` with:
- An abstract method `make_sound()`
- An abstract method `move()`

Then create concrete classes:
- `Cat` - implements `make_sound()` as "Meow" and `move()` as "Cat walks on four legs"
- `Fish` - implements `make_sound()` as "Bubble" and `move()` as "Fish swims in water"

### Exercise 5.2: Create an abstract PaymentProcessor
Create an abstract base class `PaymentProcessor` with:
- Abstract method: `process_payment(amount)`
- Abstract method: `refund(amount)`

Create concrete implementations:
- `StripeProcessor` - implement both methods with Stripe-specific messages
- `PayPalProcessor` - implement both methods with PayPal-specific messages

---

## 6. Magic Methods

### Exercise 6.1: Create a Vector class
Create a class `Vector` representing a 2D vector with:
- Attributes: `x` and `y`
- `__str__()` method to return "Vector(x, y)"
- `__add__()` method to add two vectors
- `__sub__()` method to subtract two vectors
- `__eq__()` method to check if two vectors are equal

### Exercise 6.2: Create a ShoppingCart class
Create a class `ShoppingCart` with:
- A private list of items (each item is a dict with `name` and `price`)
- `__len__()` method to return the number of items
- `__str__()` method to return a formatted list of items
- `add_item(name, price)` method
- `__getitem__(index)` method to access items by index

**Bonus:** Add `__iter__()` to make the cart iterable.

---

## Challenge Projects

### Project 1: Library Management System
Create a system with:
- `Book` class (title, author, ISBN, available status)
- `Member` class (name, member ID, borrowed books list)
- `Library` class that manages books and members
- Methods to borrow/return books, add new books, register members

### Project 2: Bank System
Create a banking system with:
- Abstract `Account` class
- `SavingsAccount` and `CheckingAccount` classes with different interest rates
- `Customer` class that can have multiple accounts
- `Bank` class that manages customers and accounts
- Transaction history tracking

---

## Submission

Feel free to share your solutions or ask questions:
- Open an issue on this repository with your solution
- Email solutions to [Kubomuedwin@gmail.com](mailto:Kubomuedwin@gmail.com)

**Tips for Success:**
- Start with the basic exercises and progress to harder ones
- Run your code frequently to test it
- Don't be afraid to look back at the tutorial files for help
- Try to solve exercises before checking solutions
- Experiment with adding extra features to make the exercises your own!

Good luck and happy coding!
