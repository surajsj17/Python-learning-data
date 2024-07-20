# Example: 1
#Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
print("hello")

try:
    age = int(input("Enter the age:"))
    if(age<18):
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")
print('Thank you visit again...')
#Example-2:
try:
     num = int(input("Enter a positive integer: "))
     if(num <= 0):
# we can pass the message in the raise statement
         raise ValueError("That is  a negative number!")
except ValueError as e:
     print(e)

