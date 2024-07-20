# oops: object oriented programming system.
# class: it's a blueprint of an object.
        #template of an object
        #design of an object.
# it's a user defined data type. collection of data members(attribute)
# and methods(behaviour).

a = 10  # int class
l = list()
l1 = [1,2,3,4]
# class : it's a blueprint of an object.
# object: it's a real world entity.

# function
def abc():
    pass   
# class ClassName:
#     # attributes
#    # methods
#      function
        # def abc():
        # pass 

print(dir(list))


class Person:
    # attributes: it's a variable that can be used to store data. # data member
    # methods: it's a function that can be used to perform operations.
   name = 'sachin'
   age = 22
   address = 'jaipur'

   def display(self):
       return f' my name is {self.name} age is {self.age} address is {self.address}'

    
# object :
p1 = Person()
print(p1.name)
print(p1.display())

p1.name = "john"
print(p1.display())

class Car:
    name = 'audi'
    brand = 'german'    
    model_year = 2020

    def drive(self):
        return '{self.name} is moving'
    def display(self,color):
        gear_type = 'manual'
        return f'car name is {self.name} brand is {self.brand} color is {color}     {color}'


x = 10 # global variable
def display():
    global x
    x = "hello"  # local
    return x
print(x) # 10
print(display()) # hello
print(x)  # 10


# constructor: it's a special method which is used to initialize 
# the object.
# __init__ : constructor_name

# emp --> class
# method --> get_salary(emp_name),get_deprt,get_mgr

emp_data = {'john':{'salary':50000,'dept':'IT','mgr':'sachin'},
            'smith':{'salary':60000,'dept':'HR','mgr':'john'},
            'scott':{'salary':70000,'dept':'IT','mgr':'rob'}
            }
print(emp_data['john']['salary'])
class Employee:     
    def get_salary(self,emp_name):
        return emp_data[emp_name]['salary']
    def get_dept(self,emp_name):
        return emp_data[emp_name]['dept']
    def get_mgr(self,emp_name):
        return emp_data[emp_name]['mgr']
    
e1 = Employee()
print(e1.get_salary('john'))

print(e1.get_dept('john'))

e2 = Employee()
print(e2.get_salary('smith'))

e3 = Employee()
print(e3.get_mgr('scott'))

class Employees:
    def __init__(self,emp_name):
        self.emp1_name = emp_name
        print('I am constructor')

    def get_salary(self):
        return emp_data[self.emp1_name]['salary']
    def get_dept(self):
        return emp_data[self.emp1_name]['dept']
    def get_mgr(self):
        return emp_data[self.emp1_name]['mgr']
    
j = Employees('john')
print("john sal:",j.get_salary())
print(j.get_dept())

s = Employees('smith')
print("smitdept",s.get_dept())

class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

c = calc(10,20)
print(c.add())
print(c.sub())
print(c.mul())

# oops concept
# inheritance: it's a mechanism by which one class can inherit the another class.
# parent class,superclass,base class: it's a class which is being inherited.
# child class,subclass,derived class: it's a class which is inheriting the parent class.
# Types of inheritance:
# 1. single inheritance : one class is inheriting another class. 
# 2. multiple inheritance
# 3. multilevel inheritance
# 4. hierarchical inheritance
# 5. hybrid inheritance

# single inheritance
class Parent:
    middle_name = 'kumar'

    def display(self,name):
        return f"{name} {self.middle_name}"

class Child(Parent):

    def child_method(self,name):
        return f"my name is {name} {self.middle_name} and I am son of {self.display('roy')}"
        

c1 = Child()
print(c1.display('john'))
print(c1.child_method('smith'))

# multilevel inheritance
class Parent:
    surname = 'kumar'

    def display(self,name):
        return f"{name} {self.surname}"

class Child(Parent):
    middle_name = 'roy'
    def child_method(self):
        return f"my name is {self.middle_name} {self.surname} "

class GrandChild(Child):
    def grand_child_method(self,name):
        return f"my name is {name} {self.middle_name}{self.surname}
            
g = GrandChild()
print(g.grand_child_method('ALEX'))


# multiple inheritance: one class is inheriting multiple classes.

class vehicle:  # parent class
    def vehicle_method(self):
        return 'vehicle is moving'
class car:  # parent class
    def car_method(self):
        return 'car is moving'