# write the program for to check given number is positive or negative

num = int(input("Enter the number to check the positive or negative number :"))

if num > 0 :
    print("The number is positive : ",num)
elif num < 0 :
    print("The number is negative : ",num)
else:
    print ("The number is zero : ",num)    
    
    
'''
OUTPUT - Enter the number to check the positive or negative number :39
         The number is positive :  39
         
         Enter the number to check the positive or negative number :-23
         The number is negative :  -23        
'''