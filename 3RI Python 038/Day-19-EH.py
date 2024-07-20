# exception handling
#errors : something thet goes wrong in the program is called error
# synatx : error, logical, errors,runtime errors



# balance = 10000

# try:
#     amount = int(input("Enter amount for withdraw: "))
#     if amount <= balance:
#         balance -= amount
#         print("The transaction has been successful!!!")
#         print(f"Remaining balance: {balance}")
#     else:
#         print("Reason: Funds are insufficient Amount")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")


# try:
#     num = int(input("Emter the number :"))
#     num1 = int(input("Emter the number :"))
#     print(num/num1)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Invalid input. ZeroDivisionError")
    
    
# try: 
#     x = int(input(" Enter the number : " ))
#     y = int(input(" Enter the number : " ))
#     value = x/y
#     print(value)                                #exception
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Invalid input. ZeroDivisionError")
# else:
#     print("There is no error")
#     if value % 2 == 0:
#         print("The value is even number")
#     else:
#         print("The value is odd number")
# finally:
#     print("This is finally block")
    
    
# assert : it's a keyword thet can be used to check a condition
#assert condition ,message
# if condition is true it will not display any message

# a = 10 
# b  = 20
# assert a>b

# print(dir(__builtins__))  # it is used to check built functions


# l1 = [10,20,30,40]
# index = int(input("Index number : "))
# # breakpoint()
# if index < len(l1):
#    print(l1[index])  
# else:
#    raise Exception("Index number out of range")    


# if 10 > 20 : raise Exception("10 is not greater than 20")


#prime number

# list = [22, 3, 4, 6, 11]
# for i in range(2, len(list)):
#     if list[i] % i == 0:
#         print(list[i])
#         break
# else:
#     print("not prime", list[i])
    
    
             