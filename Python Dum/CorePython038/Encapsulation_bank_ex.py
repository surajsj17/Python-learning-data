"""Encapsulation is a fundamental concept in
object-oriented programming
that allows bundling of data (attributes) and methods (functions)
together within a class.

It promotes the idea of data hiding, where the internal details of a class
are hidden from external access,
and interactions with the class are done through a well-defined interface."""

# Python doesn't strictly enforce access modifiers like some other languages,
# but the use of naming conventions helps indicate the data hiding

class Bank:
    __bank_name = 'HDFC' # private

    def __init__(self, name, balance):
        self.__name = name  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount} successfully.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name


# Creating an instance of the Bank class
account = Bank("John Doe", 1000)

# Attempting to access private attributes directly
print(account.__name)  # This will raise an AttributeError
#print(account._Bank__bank_name) # access using class name _cls_name
#print(Bank._Bank__bank_name)
# Accessing private attributes via getter methods
print("Account Holder:", account.get_name())
print("Initial Balance:", account.get_balance())

# Depositing and Withdrawing money
account.deposit(500)
print(account.get_balance())
account.withdraw(200)

# Checking updated balance
print("Updated Balance:", account.get_balance())


