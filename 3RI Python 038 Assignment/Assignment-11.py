# write the program to the factorial number 

number = int(input("Enter the number : "))

factorial = 1

for i in range(1, number+1):
    factorial = factorial * i
print("The factorial number of",number,"is",factorial)

'''
OUTPUT - Enter the number : 5
         The factorial number of 5 is 120
'''