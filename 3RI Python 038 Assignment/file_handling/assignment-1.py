#1)	find no of characters, no  of words or number of lines in Python text file.

# f = open ("text.txt","x")
# f.writelines(['\nfirst line','\nsecond line','\nthird line'])

# f = open ("text.txt","r")
# chara = f.read()
# counter = 0
# for i in chara:
#     counter = counter + 1
# print (counter)

'''
OUTPUT : 60
'''

# with open ("text.txt","r") as f:
#     chara = f.readline()
# counter = 0
# for word in chara:
#     counter = counter + 1
# print (f"There are {counter} word in text file")

'''
OUTPUT :
        There are 11 word in text file
'''

with open ("text.txt","r") as f:
    chara = f.readlines()
counter = 0
for word in chara:
    counter = counter + 1
print (f"There are {counter} lines in text file")

'''
OUTPUT : There are 8 characters in text file
'''