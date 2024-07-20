# write the program to check whether number even or odd numbers

num = int(input("Enter the number :"))

if num == 0:
    print ("The number is invalid")
elif num % 2 == 0:
    print ("The number is Even number :",num)
else:
    print("The number is odd number :",num)
    
'''
OUTPUT - Enter the number :23
         The number is odd number : 23
         
         Enter the number :2
         The number is Even number : 2
'''