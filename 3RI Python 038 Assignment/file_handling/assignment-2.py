# 2)	Write a program to Count the number of upper-case alphabets present in a text file “PYTHON.TXT”.
# Ex: We Learn Python.   3 isupper() 


# f = open("PYTHON.TXT","x")  
# f = open("PYTHON.TXT","w")
# f.writelines(["PYTHON\nProgram\nlanguage"])

with open("PYTHON.TXT","r") as f:
    char = f.read()
counter = 0
for i in char:
    if i.isupper():
        counter += 1
    else:
        pass
print(f"There are {counter} alphabets in upper-case ")

'''
OUTPUT - There are 7 alphabets in upper-case 
'''
