# write the program to find the vowels is there in string or not [count]

string = input("Enter a string :")

vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print ("This string have vowels :", count)

'''
OUTPUT: 
Enter a string :suraj
This string have vowels : 2
'''

