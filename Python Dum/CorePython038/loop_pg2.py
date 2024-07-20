# for loop:  it is used to iterate over a sequence (list, tuple, string) or other iterable objects.
#synatx:
# for  iterator_var in sequence:
#     statement1
# wap to print 1 to 10 int numbers.
for i in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    print(i)

# wap to print 10 to 1 int numbers.
# range(10,0,-1)  # 10,9,8,7,6,5,4,3,2,1

print(range(10))  # range(0,10)

# wap to find sum of 1 to 10 int numbers
total = 0
for i in range(1,11):
    total+=i  # total = total + i
print("sum of 1 to 10 int numbers is :",total)

# jumping Statement
# break : it is used to terminate the loop.
# continue : it is used to skip the current iteration.
# pass : it is used to do nothing.

# wap to print 1 to 10 int numbers but stop the loop when i= 5.
for i in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    if i == 5:  # 1 == 5 --> False #2==5-->False #3==5-->False #4==5-->False #5==5-->True
        break
    print(i)
print("loop is terminated")    
# continue:
# wap to print 1 to 20 int numbers but skip the number 5 ,15,20. 
for i in range(1,21): # 1,2,3,4,5,6,7,8,9,10
    if i ==5 or i ==15 or i==20: # 1 == 5 --> False #2==5-->False #3==5-->False #4==5-->False #5==5-->True
        continue
    print(i)




  

# hw.
#2. write a python program to check entered number is even or odd.
#3.write a python program to check entered year is leap year or not.
#for leap year, year should be divisible by 4 and 400 but not by 100
# 4.write a python program to check entered number is positive or negative.
# 5. write a python program to check entered number is armstrong or not.
# armstrong numbers means sum of cube of each digit is equal to
# the number itself. eg: 153 = 1^3+5^3+3^3 = 153.  # 22--> 2^3 + 2^3 = 16+8 = 24

#6. write a python program to check entered number is palindrome or not.
# palindrome number means number is same from left to right and right to left.
# eg: 121, 12321, 1234321, 123454321 (/,%,//)
#7. write a python program to check entered number is perfect number or not.
# perfect number means sum of all divisors of number is equal to number itself.
# eg: 6 = 1+2+3 = 6, 28 = 1+2+4+7+14 = 28


