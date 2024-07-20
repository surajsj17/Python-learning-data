# write the program to print 2 entered number 


num = int(input("Enter the first number  :"))
num1 =int(input("Enter the secound number :"))

counter = num
while counter <= num1:
    print(counter)
    counter+=1
if counter > num1:
    print("Invalid number")
    exit ()
    
'''
    OUTPUT =
    Enter the first number  :2
Enter the secound number :4
2
3
4
'''
        
        
    
    