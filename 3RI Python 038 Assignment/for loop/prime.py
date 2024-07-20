# write the program to print the entered prime number or not

num = int(input("Enter the number :"))

for i in range(2,num):
    if num % i == 0:
        print ("This number is not prime number :", num)
        break
else:
    print("This number is prime :", num)
    
    
'''
OUTPUT - 
Enter the number :7
This number is prime : 7

'''