#write the program to match last character of string with number

import re

string = input("Please enter the string: ")
regex = r'[0-9]$'
if re.search(regex, string):
    print("The last character of the string is a number")
else:
    print("The last character of the string is not a number")


'''
OUTPUT - 
        Please enter the string: python333
        The last character of the string is a number
'''