# oops
# encapsulation
# inheritance
# ploymorephisum
# abstraction
# object
# class

# class : class is blueprint or template of any object
# that define property(attribute) and # method(functionallity).

# object : instance of class.real world entity of concept

l1 = [1,2,3,4,5,6]
print(type(l1)) # class list [,,] -->l1 =[1,2,3]
print(dir(l1))


# class Cls_name:
    # attributes
    #methods(function)

class Car1:
    data = "This is car class atrribute"
    def car_details(self):
        print("I am a method of car class")

#how to create objects
c1 =Car1()
print(c1.data)
c1.car_details()

# change attribute value
c1.data = "this is car"
print(c1.data)




# how to create a class in python
class Car:
    data = "this is car class" # attribute

    def __init__(self): # constructor(special method) used to construct features of object.
        self.name = 'Audi' # instance attribute
        self.model = "x7"
# self : self is keyword which is pass as a first parameter in method and
# used to refer to the obj.
# refering to object it is point to object
#object to which method  is called.
# object
a1 = Car()
print(type(a1))
print(a1.data) # "this is car class"
a1.data = "hello"
print("change attribute value",a1.data)
print(a1.name)
print(a1.model)

class HondaCity:
    def __init__(self):
        self.name = "honda"
        self.model = "city"

c1 = HondaCity()
print(c1.name)
print(c1.model)


# car
# parameterized class or class

class Car:
    def __init__(self,name,model): # parameterized  constructor
        self.name =  name # attributes
        self.model =model

    def  start_engine(self): # method
        print("engine started")

my_car = Car("Toyoto","corolla")
print(my_car.name)
print(my_car.model)
#my_car.name = "maruti"

my_car2 = Car("Audi","x7")
my_car3 = Car("BMW","xadf")

my_car2.start_engine()
# employees_details
emp_details = {"john":{'sal':25000,"dept":"it"},
               "alex":{'sal':35000,"dept":"hr"},
               "ellena":{'sal':45000,"dept":"sales"}}
print(emp_details['alex']['sal'])
# non parameterized class
class Employee:
    def get_salary(self,emp_name):
        salary = emp_details[emp_name]['sal']
        print("salary for emp",emp_name,"is",salary)
    def get_dept (self,emp_name):
        department = emp_details[emp_name]['dept']
        print("department of emp:",emp_name,"is",department)

E1 = Employee() # E1 object
E1.get_salary("alex")
E1.get_dept("alex")

#E1.get_re_mgr("alex")
#E1.get_dept("ellena")
#E1.get_re_mgr("emp1")

# parameterized class
print("#"*50)
class Employees:
    def __init__(self,emp_name): # constructor is a special method
        self.emp_nm = emp_name
        print("These are employees details class.")
    def get_sal(self):
        salary = emp_details[self.emp_nm]['sal']
        print("salary for emp",self.emp_nm,"is",salary)
    def get_dept (self):
        department = emp_details[self.emp_nm]['dept']
        print("department of emp:",self.emp_nm,"is",department)

# how to call
e1 = Employees("john") # emp_name
e1.get_sal()
e1.get_dept()

e2 = Employees("alex")
e2.get_dept()
#e2.get_sal()


