# write the program and enter the operator with 2 numbers by user

num1 = float(input("Enter a number :"))
num = float(input("Enter a number :"))
operater = input("Enter the operator = + , - , * , / , // , **,  : "  )

if operater == "+":
    result = num1 + num
    
elif operater == "-":
    result = num1 - num
    
elif operater == "*":
    result = num1 * num
    
elif operater == "/" :
    if num != 0:
        result = num1 / num
    else:
        print("ERROR: Division by zero")  
        exit ()
elif operater ==  "//" : 
    if num != 0:
        result = num1 // num
    else:
        print("ERROR: Division by zero")
        exit ()
elif operater == "**" :
    result = num1 ** num

print("Result : ",result)
     
'''
OUTPUT - Enter a number :5
         Enter a number :2
         Enter the operator = + , - , * , / , // , **,  : //
         Result :  2.0
'''