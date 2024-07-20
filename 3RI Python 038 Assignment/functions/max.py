# write the program to find the max number of 3 by using function


def max(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print("The max number : ", max(20,40,10))

'''
OUTPUT - 
The max number :  40
'''

