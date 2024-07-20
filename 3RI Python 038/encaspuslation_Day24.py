# encapsulation is one of the fundamental concepts


class Employee:
    public = "Hello world"
    def __init__(self,_name,__salary):
        self._name = _name # protected
        self.__salary = __salary # private
    def get_name(self):
        return self._name
    def get_salary(self):
        return self.__salary
    def set_salary(self,new_salary):
        self.__salary = new_salary
    
#creating an instance of employee class
emp = Employee("john" , 20000)
print(emp.get_name())
print(emp.public)
emp.public ="good morning"
print(f"After changing the public : {emp.public}")
print (emp._name)
print ()