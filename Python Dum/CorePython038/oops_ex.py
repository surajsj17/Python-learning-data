# how to create class

#syntax:
'''
class Cls_name:
    data,methods
'''
class Employees:
    company = '3ritech'  #  class attributes,data,charactristics

    def __init__(self,name,age,dept): # initialization
        self.name = name  # instance attribute
        self.age = age
        self.dept = dept

    def display(self):
        print(f'My self.name)

emp1 = Employees("john",23,'IT') # object (instance)
emp2 = Employees("alex",24,'hr')

print(emp1.company)

print(f"hello my name is {emp1.name} I am from {emp1.dept} and my age is {emp1.age}")
print(emp2.company)
print(f"hello my name is {emp2.name} I am from {emp2.dept} and my age is {emp2.age}")


# how to create object
#emp1 = Employees()




