# write the program to check the prime number 


num = int(input("Enter the number : "))


for i in range(2,num):
    if num % i == 0:
        print("The number is not a prime number : ",num)
        break
else:
 print("The number is a prime number : ",num)
            
'''
OUTPUT - Enter the number : 7
         The number is a prime number :  7
'''