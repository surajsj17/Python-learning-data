# 4)	Write a program to count the words “to” and “the” present in a text file “python.txt”.

#f = open("python4.txt","x")

# f.writelines("Write a program to count the words to and the present in a text file ")
f = open("python4.txt","r")
char = f.read()
words = char.split()
to = 0
the = 0
for word in words:
    if word == "to":
        to = to + 1
    elif word == "the":
        the = the + 1
    else:
        pass
print (f"Count of letter = to : {to}")
print (f"Count of letter = the : {the}")

'''
output -
        Count of letter = to : 2
        Count of letter = the : 2
'''