# write the program to match first character of string with number

import re
string = input("Please enter the string : ")
regex  = '[0-9]'

if re.match(regex, string):
    print("The given string start with number")
else:
    print("The given string does not match with number")
    
'''
OUTPUT - 
    Please enter the string : 123python
    The given string start with number
'''
