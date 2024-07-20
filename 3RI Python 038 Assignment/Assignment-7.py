# write the program to check the number is armstrong or not 

number = int(input("Enter the number :"))
order = len(str(number))  # len() is inbuild function but it work on string so we need to covert to (str(number))

sum = 0
temp = number 

while temp > 0:
    digit = temp % 10           # It will hold last value temp in digit variable 
    cube = digit ** order       # order to check how many digits in input value from user to calculate cube number
    sum = sum + cube            # sum variable will the cube number
    temp //=10                  
if sum == number :
    print ("The number is armstrong number :",number)
else:
    print ("The number is not armstrong number :",number)