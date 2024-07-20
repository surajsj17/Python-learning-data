# oops: object oriented programming
# Encapsulation
# inheritance
#polymorphisum
# Abstarction

# class: blueprint of any object,design pattern,templates
# class include attributes(property) and
# methods(functions)functionallity
# object: instance of class(existance)
#

# instance variable:
class Car:
    pass
honda = Car()
tata = Car()
 # instance varible
honda.modelname = 'city'
honda.yearm = '2004'
honda.price = 1000000

tata.modelname = 'Bolt'
tata.yearm = '2016'
tata.price = 1600000

print(honda.price)
print(tata.price)
a = 10
l1 = [1,2,3,4]
print(type(l1)) # class <list> [,,]
print(dir(l1))
# create object
l2 = list()
l3 = []
l123 = list()
# print(type(l2))
#
print(dir(list))

# class:
#class Class_Name:
    #attributes,property
    # methods,functionallity,behaviour


# how to create class
# non parameterized class
#

class CarDetails:
    name = "hondacity" # attributes,property
    colour = 'red'  #
    print("I am a class car",name)
    print("colour:",colour)

    def display_details(self,Name): # method behaviour
        print("I am display method of car",Name)
        print("I am class cardetails attribute",self.name)

    def details(self):
        print("hello all I am details method")
# how to create object
c1 = CarDetails() # c1 object

print(c1.name ) # access name attribute
c1.colour = 'white'
print(c1.colour) # white
c1.details()
c1.display_details('HONDA')








# employees_details
emp_details = {"john":{'sal':25000,"dept":"it",'re_mgr':'jenish'},
               "alex":{'sal':35000,"dept":"hr",'re_mgr':'Denish'},
               "ellena":{'sal':45000,"dept":"sales",'re_mgr':'ellen'}}
# print(emp_details['john']) # {'sal':25000,"dept":"it",'re_mgr':'jenish'}
# print(emp_details['john']['sal']) # 25000
# print(emp_details['alex']['dept']  # hr
# non parameterized class
class Employee:  # e1 = Employee()
    def get_salary(self,emp_name):
        salary = emp_details[emp_name]['sal']
        print("salary for emp",emp_name,"is",salary)
    def get_dept (self,emp_name):
        department = emp_details[emp_name]['dept']
        print("department of emp:",emp_name,"is",department)
    def get_mgr_(self,emp_name):
        mgr = emp_details[emp_name]['re_mgr']
        print("My manager is:",mgr)

E1 = Employee() # E1 object
E1.get_salary("john") #
E1.get_dept("john")
E1.get_mgr_("john") # ellen
E1.get_dept("ellena")
#E1.get_re_mgr("emp1")
E1.get_dept('ellena')

print("$$$"*100)
# parameterized class
print("#"*50)

emp_details = {"john":{'sal':25000,"dept":"it",'re_mgr':'jenish'},
               "alex":{'sal':35000,"dept":"hr",'re_mgr':'Denish'},
               "ellena":{'sal':45000,"dept":"sales",'re_mgr':'ellen'}}

class Employees:
    def __init__(self,emp_name): #
        #self.emp_name = emp_name
        self.emp_nm = emp_name
        print("These are employees details  const. class.")
    def get_sal(self):
        salary = emp_details[self.emp_nm]['sal']
        print("salary for emp",self.emp_nm,"is",salary)
    def get_dept (self):
        department = emp_details[self.emp_nm]['dept']
        print("department of emp:",self.emp_nm,"is",department)

# how to call
e1 = Employees("john") # emp_name = 'constructor'
e1.get_sal()
e1.get_dept()

e2 = Employees("alex")
e2.get_dept()
#e2.get_sal()

# dir(paramter)
print(dir(list))

# create class max_min in which define two method
# max and min also create constructor in max_min class
#and pass 2 parameters. find maximun and minimum number from
# given input parameter.




class max_min:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
        print("The maximum and minimum number is: ")

    def max(self):
        maximum = max(self.num1,self.num2)
        print("Maximum Number is: ",maximum)

    def min(self):
        minimum = min(self.num1,self.num2)
        print("Minimum number is: ",minimum)

number = max_min(10,20)
number.max()
number.min()





