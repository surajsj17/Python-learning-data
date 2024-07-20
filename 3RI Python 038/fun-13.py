# FUNCTION ()

#building function
#user-defined function

def msg():
    return "hello good morning"
print(msg())

def msg1():
    print("hello good morning")
msg1()

# num = int(input("Enter the number : "))
# num1 = int(input("Enter the number : "))

# def add():
#     num + num1
#     return num + num1 

# print("Addition of 2 number : " , add())

def squre(num):
    num ** 2
    return  num ** 2 
print(squre(3) ,squre(2))
print(squre(5))

# keyword arguments (name arguments)

# def emp(name,age,company):
#     return f"employe name is {name} 
#     and age is {age} and company name is {company}"

# print(emp("sky" , 24 , "BCCI"))
# print(emp(name="hitman",age="45",company="BCCI"))

#default arguments
def student(name,email,course="python"):
    return f"student name is {name} and email is {email} and course is {course}"

print(student("jenny","abcgmail.com"))



# 4 vaiable -length arguments
# only list and tuple will pass not dict 
def addition(*args):
    counter = 0
    for i in args:
        counter = counter + i
    return counter
args = 1,2,3,4,5,6,7,8,9,10,11
x =(1,2,3)
l = [1,2,3,4,5]
print(addition(*args))
print(addition(20,40))
print(addition(*(10,20,30,40)))
print(addition(*(x)))
print(addition(*(l)))
print(addition(*args [0:6]))

#keyword variable - length argument

def emp_details(**date):
    for key,value in date.items():
        print(f"{key} : {value}")
emp_details (name='suraj',age =24,location = "pune")
emp_details (**{ 'name':'sumeth','age':24,'location':'pcmc','dept':'IT'})
    


