#write the program to print factroials number of entered using for loop

num = int(input("Enter the number : "))

fact = 1 
for i in range(1,num+1):
    fact = fact * i
print ("The factroials number :" , fact)

'''
OUTPUT - 
Enter the number : 5
The factroials number : 120
'''
    