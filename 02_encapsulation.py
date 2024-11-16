class Account:
    """
    This class demonstrates encapsulation in Object-Oriented Programming (OOP).

    The class hides the internal state of the account (balance) by making it private 
    and provides public methods to interact with the balance (deposit, withdraw, and get_balance).
    
    The balance cannot be directly accessed or modified from outside the class, ensuring 
    that it can only be manipulated through the provided methods, maintaining control 
    over how the data is modified.
    """

    def __init__(self, owner, balance=0):
        """
        Initialize the Account object with an owner's name and an optional initial balance.

        Args:
            owner (str): The name of the account owner.
            balance (float, optional): The initial balance in the account. Default is 0.
        """
        self.owner = owner  # Assign the account owner
        self.__balance = balance  # Private attribute to store account balance

    def deposit(self, amount):
        """
        Deposit a positive amount into the account.

        Args:
            amount (float): The amount to deposit into the account.
        
        Returns:
            None: Updates the account balance with the deposited amount.
        """
        if amount > 0:  # Ensure that the deposited amount is positive
            self.__balance += amount  # Increase the balance by the deposit amount

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account, if sufficient balance is available.

        Args:
            amount (float): The amount to withdraw from the account.
        
        Returns:
            None: Reduces the balance if withdrawal is successful; prints an error message if insufficient funds.
        """
        if 0 < amount <= self.__balance:  # Ensure amount is positive and there is enough balance
            self.__balance -= amount  # Decrease the balance by the withdrawal amount
        else:
            print("Insufficient balance.")  # Error message for insufficient funds

    def get_balance(self):
        """
        Retrieve the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self.__balance  # Return the private balance value

# Create an Account object for John with an initial balance of 0
account1 = Account("John")

# Deposit 1000 units to the account
account1.deposit(1000)

# Print the account balance using the getter method
print(account1.get_balance())  # Access the balance via the getter method
