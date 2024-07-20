# write the program to check entered values is even or odd 

number = int(input("Enter the Number :"))

if number % 2 == 0:
    print("The entered value is even number  :",number)
else:
    print ("The entered value is odd number :",number)
    
'''
OUTPUT: Enter the number : 20
        The entered value is even number  : 20  
'''
    
#write the program to check entered 2 values as input is even or odd {using for loop and with range functions}

num = int(input("Enter the starting number :"))
num2= int(input("Enter the ending number :"))

if num >= num2 :
    print("Please entered valid number")
    exit ()
else:
    for i in range (num,num2+1):
        if i % 2 ==0:
            print("Even number :",i)
        else:
            print("Odd number :",i)

'''
    OUTPUT - Enter the starting number :10
    Enter the ending number :20
    Even number : 10
    Even number : 12
    Even number : 14
    Even number : 16
    Even number : 18
    Even number : 20
    Odd number : 11
    Odd number : 13
    Odd number : 15
    Odd number : 17
    Odd number : 19
'''



