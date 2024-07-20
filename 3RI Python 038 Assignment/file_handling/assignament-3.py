# 3)	A text file “PYTHON.TXT” contains alphanumeric text. Write a program that reads this 
# text file and writes to another file “PYTHON1.TXT” entire file except the numbers or digits in the file

# file = open( "PYTHON1.TXT","x")

with open ("PYTHON.TXT", "r") as f:
    char = f.readlines()
    
new_file = open ("PYTHON1.TXT","w")
counter = 0
for word in char:
    if word.strip().isalpha():
        new_file.write(word)
        counter += 1
    else:
        pass
print (f"There are {counter} alphabetic")    

'''
Output - 
There are 3 alphabetic
'''