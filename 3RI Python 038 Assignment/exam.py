num = int(input("enter the number :"))

data = len(str(num))
sum = 0

temp = num

#153
while temp > 0:
    digit = temp % 10
    cube = digit ** data
    sum = sum + cube
    temp //=10
if sum == num :
    print ("the p")
else:
    pass   