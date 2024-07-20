# os: operating system dependent functionality
import os,datetime

# getcwd() : get current working directory path
# print(os.getcwd())
# # listdir() : list all files and directories in the 
# #current working directory
# print(os.listdir())
# print(os.listdir(r"D:\3riSuvidha"))

# print("hello\nworld")

# mkdir() : make a directory (folder)
# os.mkdir("test")
# os.mkdir(r"D:\3riSuvidha\test1")

# rmdir() : remove a directory
#os.rmdir("test")
#os.rmdir("D:\\3riSuvidha\\newfolder\\test1")
# \n 
# \t
# remove() : remove a file
#os.remove("demo.py")

# rename() : rename a file or directory
# os.rename("calc.py", "calculator.py")
# os.rename("calculator.py", "calc.py")

# datetime module
import datetime 
print(datetime.datetime.now())  # yyyy-mm-dd hh:mm:ss.ffffff
# yyyy-mm-dd hh:mm:ss
print(datetime.datetime.now().date())  # yyyy-mm-dd 

# date class
dt = datetime.date(2021, 12, 31) # yyyy-mm-dd
print(dt)
print(type(dt))
# strftime() : string format time
print(dt.strftime("%d-%B-%Y")) # december
print(dt.strftime("%d-%b-%Y")) # dec

import math
print(math.sqrt(25))
print(math.pow(2,3))
print(math.pi) # 3.14
print(math.sin(90))
#floor() : floor value of a number(nearest lower integer)
# ceil() : ceil value of a number(nearest higher integer)
print(math.floor(10.9))  # 10
print(math.ceil(10.1))   # 11

# abs() : absolute value
print(abs(-10))  # 10

# reduce() : reduce a sequence to a single value
#syntax: reduce(function, iterable)
l1 = [10,20,30,40,50]
# sum of all elements in the list
from functools import reduce
result = reduce(lambda a,b: a+b, l1)
print(result)

import random 
# randint() : random integer between two numbers
# random() : random float between 0 and 1

print(random.randint(10,20))
print(random.random())

import calendar

print(calendar.month(2024, 5))
print(calendar.calendar(2024))

