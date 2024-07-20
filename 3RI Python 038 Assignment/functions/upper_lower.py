# write the program to find the upper and lower case letters

string = input("enter the string : ")
def check(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1 
        elif i.islower():
            lower += 1
        else:
            pass
    return upper,lower
upper_count,lower_count = check(string)
print ("The Upper letter count : ", upper_count)
print ("The lower letter count : ", lower_count)

'''
OUTPUT - 
enter the string : SuarJ
The Upper letter count :  2
The lower letter count :  3

'''

