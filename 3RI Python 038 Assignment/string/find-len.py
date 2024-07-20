# write the program to find the len for entered string without len() function

string = input("Enter a string :")

counter = 0
for i in string:
    counter = counter + 1
print ("The length of give string : ",string," = ",counter)


'''
OUTPUT - 
Enter a string :python
The length of give string :  python  =  6
'''