# write the program to check the greater 2 number and take input from user.

num = int(input("Enter the first number : "))
num1 = int(input("Enter the second number : "))

if num ==  num1:
    print ("The number is equal to the first number and the second number")
elif num > num1:
    print ("The first number is greater than the second number :",num)
else:
    print("The second number is greater than the first number :",num1)
    
'''
OUTPUT - Enter the first number : 45
         Enter the second number : 56
         The second number is greater than the first number : 56
'''