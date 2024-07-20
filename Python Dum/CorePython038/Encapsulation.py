# Encapsulation
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
# It describes the idea of wrapping data and the methods
# that work on data within one unit.
# This puts restrictions on accessing variables and methods
# directly and can prevent the accidental modification of data.
# To prevent accidental change, an object’s variable can only be changed by an object’s method.
# Those types of variables are known as private variable.
# A class is an example of encapsulation as it encapsulates 
#all the data that is member functions, variables, etc.

# Encapsulation is defined as the wrapping up of data under a single unit.

class student:
    name = "john" # public variable
    __age = 23 # private variable
    _sub = "maths" # protected variable
s = student()
print(s.name) # john
print(s.__age) # AttributeError: 'student' object has no attribute '__age'
print(s._sub) # maths
s.name = "alex"
print(s.name) # alex

class Car:
    def __init__(self, brand, model, color):
        self.__brand = brand
        self.__model = model
        self.__color = color

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", "Blue")

# Accessing the private variables using getter methods
print(my_car.get_brand())  # Output: Toyota
print(my_car.get_model())  # Output: Camry
print(my_car.get_color())  # Output: Blue

# Trying to access the private variables directly
# This will result in an AttributeError
print(my_car.__brand)  # Raises AttributeError

# Changing the color of the car using the setter method
my_car.set_color("Red")

# Accessing the updated color using the getter method
print(my_car.get_color())  # Output: Red

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private variable
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

# Creating an instance of the BankAccount class
my_account = BankAccount("1234567890", 1000)

# Accessing the private variables using getter methods
print(my_account.get_account_number())  # Output: 1234567890
print(my_account.get_balance())  # Output: 1000

# Trying to access the private variables directly
# This will result in an AttributeError
print(my_account.__account_number)  # Raises AttributeError

# Depositing money into the account
my_account.deposit(500)

# Withdrawing money from the account
my_account.withdraw(200)

# Accessing the updated balance using the getter method
print(my_account.get_balance())  # Output: 1300