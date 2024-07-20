
# import Module of OS
import os,datetime
print(os.listdir())
print(os.listdir(r"H:\python work"))  # list of directories
#print(os.mkdir(r"H:\python work\test"))   # create directory
#print (os.rmdir(r"H:\python work\test"))   #remove directory   

#print (dir(os))
print(datetime.datetime.now())   # date and time
print(datetime.datetime.now().date())  # date
print(datetime.datetime.now().time()) # time

dates = (datetime.datetime.now().date())  # date with variable 
print("Today date  : ",dates)

date = datetime.date(2024,6,17)
print("date : ",date)


# strftime(): string format times
print(date.strftime("%d-%B-%Y"))

import math                # math module
print(math.sqrt(50))
print(math.pow(10,3))
print(math.floor(12.9))

#abs () it will convert the nev to positive numbers
print(abs(-10))

from functools import reduce    # reduce module

l = [1,2,3,4]
result = reduce(lambda x,y,c,d: x+y+c+d,l)
print("The sum : ",result)


import random 

print(random.randint(1,10))  #  it will give you the range of numbers any number
print(random.random())    # it will give you random numbers in  floot   

import calendar

print(calendar.month(2024,5))
print(calendar.calendar(2024))



