class EncapsulationExample:
    name = "python"
    __dept = "It" # private
    def getdept(self):
        return self.__dept
    def setdept(self,new_dept):
        self.__dept = new_dept
    def __init__(self, value):
        self.__private_value = value  # private variable
    #public method
    def get_private_value(self):
        return self.__private_value  # private variable getter

    def set_private_value(self, new_value):
        self.__private_value = new_value  # private variable setter

    def __private_method(self):
        return "This is a private method.",self.__private_value  # private method

    def public_method(self):
        return f"The value is {self.__private_value}. {self.__private_method()}"


# Example usage
obj = EncapsulationExample(100)
# Accessing private variable using getter method
print("get_method",obj.get_private_value())
# Trying to access private variable directly (will result in an error)
print(obj.name) # python
#print(obj.__dept)
#print(obj.__private_value)
# Using public method to access private variable and method
print(obj.public_method())
# Trying to access private method directly (will result in an error)
#print(EncapsulationExample.__private_method())
# print(obj.__dept)
# print(EncapsulationExample.__dept)
print(obj.getdept())
obj.setdept('HR')
print(obj.getdept())