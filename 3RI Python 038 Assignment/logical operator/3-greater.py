# write the program to find 3 greater numbers

num = int(input("Enter the first number :"))
num1 = int(input("Enter the second number :"))
num2 = int(input("Enter the third number :"))

if num > num1 and num > num2:
    print(" The first number is greater = ",num)
elif num1 > num and num1 > num2:
    print(" The second number is greater = ",num1)
else:
    print(" The third number is greater =",num2)
    
'''
OUTPUT -
Enter the first number :10
Enter the second number :2
Enter the third number :1
 The first number is greater 10
'''