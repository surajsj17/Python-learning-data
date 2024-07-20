# write the program check the entered number is perfect or not

num = int(input("Enter a number :"))

sum = 0

for i in range(1,num):
    if num % i == 0:
        print(i)                # able to check the number
        sum = sum + i
if sum == num:
    print("The entered number is perfect number :",num)
else:
    print("The entered number is not perfect number :",num)