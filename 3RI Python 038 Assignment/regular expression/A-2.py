#write the program to find the sequence of lowercase letter which join with underscore 


import re
string = input ("Enter the sequence of letters : ")
regex = r'\b[a-z]+(?:_[a-z]+)+\b'
patten = re.findall (regex, string)
print ("The sequence found : ",patten)


'''
Output - 
Enter the sequence of letters : the_python is programming 
The sequence found :  ['the_python']
'''

