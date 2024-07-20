# Encapsulation is one of the fundamental concepts
#in object-oriented programming (OOP).
# It describes the idea of bundling the data (attributes)
#and methods (functions) in a single unit called a class.

class Employee: 
    public = "hello"   
    def __init__(self, name, __salary):        
        self._name = name # protected
        self.__salary = __salary # private
    def get_name(self):
        return self._name
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        self.__salary = new_salary


# Creating an instance of Employee class
emp = Employee("John Doe", 50000)
print(emp.public) # hello
emp.public = "good morning" #
print("after changing public attribute value:",emp.public)
# Accessing private attributes using getter methods
# Accessing protected attributes
print(emp._name)
emp._name ="alex"
print(emp._name)
print(emp.get_name())
# # Accessing private attributes using getter methods
#print(emp.__salary)
print(emp.get_salary())

# # Modifying protected attribute using setter method
#emp.__salary = 35000
# print("*****")
print("after changing salary",emp.get_salary()) # 5000
emp.set_salary(62300)
print("after changing salary",emp.get_salary()) # 62300

# emp._name ="suvidha"
# print(emp.get_name())



# """
# Using the getter and setter methods, 
# we can interact with the encapsulated data of the Employee class 
# in a controlled manner,
# hiding the internal implementation details and
# providing an interface for accessing and modifying the private attributes.
# """

# class abc(Employee):
#     pass

# a1 = abc('alex',35500)
# print(a1.get_name())
# print(a1.get_salary())