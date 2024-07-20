# write the program to check that string contains only a certain set of characters (in this a-z ,0-9 and A-Z)

import re
string = input("Please enter the string : ")
regex = '^[a-z A-Z 0-9]+$'
if re.match(regex, string):
    print("The input string is matches")
else:
    print("The input string is not matches")
    


def regex(string):
       regex = '^[a-z A-Z 0-9]+$'
       if re.match(regex, string):
         print("The input string is matches")
       else:
         print("The input string is not matches")
string = input("Enter the string : ")
result = regex(string)

'''
OUTPUT - 
        Enter the string : SurAJ023
        The input string is matches
'''