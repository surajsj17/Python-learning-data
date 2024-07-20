# write a program to print entered n number of time 


num = int(input("Enter the Number :"))
string = input("Enter the named : " )
counter = 0

while counter < num:
    print(string)
    counter = counter + 1
    
    

# 2nd way to do program
num1 = int(input("Enter the Number : " ))
result = "Hello World  " * num
print (result)

'''
OUTPUT 
Enter the Number : 3
Hello World  Hello World  Hello World
'''