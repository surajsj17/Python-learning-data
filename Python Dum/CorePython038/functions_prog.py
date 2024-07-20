# functions: it's a block of code that performs a specific task.
# used for code reusability.
# syntax: def function_name(parameters):
#             statement
#             return value (optional) print

# buit-in functions:
# user-defined functions:

# how to call function:
# function_name(parameters)
# msg() : hello gm all
def msg(): 
    return "hello gm all"

print(msg()) # call function

def msg1():
    print("hello gm all we learn python")

msg1()
# function with parameters
def add(a,b):  # parameters
    return a+b 

print(add(12,20)) # 32  # arguments # actual arguments

def sub(a,b):
    return a-b

print(sub(20,10)) # 10

print(add(200,300))
print(add("hello ", "world"))

# a = 10
# print(a+=1) # a = a+1 # a=11
# print(a=+1) # error
 #** : power 4 **2 = 16
def sqr(a,b):  # a = 4  b = 5
    return a**2 ,b**2  # a*a  # 4 **5
print(sqr(4,5)) # 16

# Types of functions arguments:
# 1. Required arguments (positional arguments)
# 2. Keyword arguments (named arguments)
# 3. Default arguments
# 4. Variable-length arguments
# 5. keyword variable-length arguments

# # 2. Keyword arguments (named arguments)
#return " my name is",name, "I am", age, "years old and my location is", location
def emp(name,age,location):
    return f" my Name is: {name}, I am {age} years old and  my Location is: {location}"

print(emp('John', 25, 'Bangalore')) # my Name is: John, I am 25 years old and  my Location is: Bangalore

print(emp(age=35, name='alex', location='Bangalore')) # my Name is: John, I am 25 years old and  my Location is: Bangalore

# 3. Default arguments
def student_details(name,email, course='sql'):
    return f"Name: {name}, Email: {email}, Course: {course}"

print(student_details('John', 'john@g.com', 'Python')) # Name: John, Email:

print(student_details("suvidha",'suvidha.3ri@gmail.com'))

# 4. Variable-length arguments (*args)
def addition(*args): # *args: tuple # 1,2  # 1,2,3
    total = 0
    for i in args:
        total += i
    return total


args = 1,2,3,4,5,6,7,8,9,10
x = (1,2,3)
l = [1,2,3,4,5]
print(addition(20,40))
print(addition(*args))
print(addition(*x))
print(addition(*l))
print(addition(*(1,5,7,23,45,67)))

print(addition(* l[0:3]))
print(addition(* args[0:6]))

#keyword variable-length arguments (**kwargs)
def emp_details(**data):
    for k,v in data.items():
        print(f"my {k} is {v}") #  (key,value)

emp_details(name='John', age=25, location='Bangalore')
emp_details(name='Alex', age=35, location='Mumbai', course='Python')    
emp_details(**{'name':'suvidha', 'age':30, 'location':'pune','dept':'IT'})
d1 = {'name':'ELLena', 'age':30, 'location':'pune','dept':'Sales'}

emp_details(**d1)

# Lambda function: anonymous function,function has no name
# syntax: lambda arguments (n): expression
a1 = lambda a,b: a+b
print(a1(10,20)) # 30

b1 = lambda a,b: print(a-b)
b1(20,10) # 10


def sq(a):
    return a**2

s1 = lambda a: a**2
print(s1(5))
print(s1(6))
#print(s1([1,2,3,4]))
# filter(function,iterable),
# map(function,iterable), : it returns map object
s = [1,2,3,4,5,6,7,8,9,10]
# wap to genereate  a new_list of square of each element of s list
square = list(map(lambda x :x**2 ,s))
print(square) # <map object at 0x7f8b1b3b3d90>


# filter : it returns filter object
# wap to filter even numbers from s list
even  = list(filter(lambda i: i%2==0,s))
print(even)
even1 = list (map(lambda i: i%2==0,s))
print(even1)
# reduce((function,iterable))


s = [1,2,3,4,5,6,7,8,9,10]
l = []
for i in s:
    if i % 2 == 0: # 1
       l.append(i) 
print(l) # [2,4,6,8,10]

# reduce()


