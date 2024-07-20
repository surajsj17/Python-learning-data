# write the program to match first character of string

# The letter match [srjSRJ]


import re
string = input("Please enter the string : ")
regex  = '[srjSRJ]'

if re.match(regex, string):
    print("The given string matches")
else:
    print("The given string does not match")
    
'''
OUTPUT - 
    Please enter the string : suraj
    The given string matches
'''
