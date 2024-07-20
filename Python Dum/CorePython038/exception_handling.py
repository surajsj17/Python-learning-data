# Exception handling:
# Errors:  something that goes wrong in the program is called error.
#Syntax errors, logical errors, runtime errors
# a = 10
# b = 20
# if a > b:
#     print('a is greater than b')
# else: 
#     print('b is greater than a')

# x = int(input("enter number"))  # 20
# y = int(input("enter number"))  # 5 # 0
# try: # suspicious code
#     print(x/y)  # 20/5 = 4.0  # 20/0
# except Exception :
#     print('you entered wrong input')


# l1 = [10,20,30,40,50]
# print(l1[0])

# Exception handling: it's a process of handling runtime errors.
# try: it's a block of code that can raise an exception.
# except: it's a block of code that can handle the exception.
# finally: it's a block of code that can be executed regardless of the exception.
# raise: it's a keyword that can be used to raise an exception.
# assert: it's a keyword that can be used to check a condition.
# else: it's a block of code that can be executed if there is no exception.
# try: # suspicious code
#     x = int(input("enter number"))  # 20
#     y = int(input("enter number"))  # 5 # 0
#     value = x//y
#     print(value)  # 20/5 = 4.0  # 20/0
# except ZeroDivisionError :
#     print('you entered wrong input')
# else:
#     print('no exception generated')
#     if value % 2 == 0:
#         print('value is even')
# finally :
#     print('this is finally block all the time executed')

# assert: it's a keyword that can be used to check a condition.
# assert condition, message
# if condition is True then it will not do anything
# if condition is False then it will raise an exception.
#  also used for debugging purpose.
# a = 50
# b = 20
# assert a>b

# print(dir(__builtins__))

# raise:

l1 = [10,20,30,40,50]
index = int(input('enter index number:'))  # 4  # 30
if index < len(l1):    # 4 < 5  # 30 < 5
    print(l1[index])
else:
    raise IndexError('index out of range')


if 10 > 20 : raise Exception('10 is not greater than 20')