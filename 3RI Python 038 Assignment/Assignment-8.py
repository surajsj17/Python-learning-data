# write the program to check entered number is palindrome or not {using while loop}

num = input("Enter a number :")
temp = num
reverse = 0

while temp > 0:                           
     digit = temp % 10               
     reverse = reverse * 10 + digit  
     temp //= 10   
if  num == reverse:
    print("The number is palindrome :",num)
else:
    print("The number is not palindrome :",num)                 
    
    
# write the program to check entered number is palindrome or not {slice index}

num = input("Enter a number :")

reverse_data = num[::-1]

if num == reverse_data:
    print("The number is palindrome :",num)
else:
    print("The number is not palindrome :",num)
