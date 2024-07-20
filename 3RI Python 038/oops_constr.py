# constructors  -  It is method to create the object

# without the constructor

employees = {'scoot' : {'salary' : 1000 ,'dept' : "IT" ,'emp_id': 102},
             'john' : {'salary' : 2000 ,'dept' : "IT" ,'emp_id': 103},
             'smith' : {'salary' : 5000 ,'dept' : "IT" ,'emp_id': 101}}

print(employees["scoot"]["salary"])

class Employee:
    def get_emp_salary(self,emp_name):
        return employees[emp_name]["salary"]
    def get_emp_dept(self,emp_name):
        return employees[emp_name]["dept"]
    def get_emp_id(self,emp_name):
        return employees[emp_name]["emp_id"]

e1 = Employee()    # creating the object
print ("Emp salary : ",e1.get_emp_salary('scoot'))
print("Emp dept : ", e1.get_emp_dept('scoot'))
print("Emp ID : ",e1.get_emp_id('scoot'))

print("*" * 10)

e2 = Employee()     # creating another object
print ("Emp salary : ",e2.get_emp_salary('john'))
print("Emp dept : ", e2.get_emp_dept('john'))
print("Emp ID : ",e2.get_emp_id('john'))

'''
OUTPUT - 
1000
Emp salary :  1000
Emp dept :  IT
Emp ID :  102
**********
Emp salary :  2000
Emp dept :  IT
Emp ID :  103

'''

print ("*"*10)

employees1 = {'scoot' : {'salary' : 1000 ,'dept' : "IT" ,'emp_id': 102},
             'john' : {'salary' : 2000 ,'dept' : "IT" ,'emp_id': 103},
             'smith' : {'salary' : 5000 ,'dept' : "IT" ,'emp_id': 101}}

class User:
    def __init__(self, username):
        self.username1 = username
        print("The Constructor")
    def get_user_salary(self):
        return employees1[self.username1]["salary"]
    def get_user_dept(self):
        return employees1[self.username1]["dept"]
    def get_user_emp_id(self):
        return employees1[self.username1]["emp_id"]

u1 = User("scoot")
print("The scoot salary : ",u1.get_user_salary())

u2 = User("john")
print ("The john salary : ",u2.get_user_salary())

'''
The constructor
The scoot salary :  1000
The constructor
The john salary :  2000
'''