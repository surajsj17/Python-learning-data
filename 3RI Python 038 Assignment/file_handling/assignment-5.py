# 5)	Write a program to display all the lines in a file “python.txt” along with line/record number.


with open("python.txt", "r") as f:
    lines = f.readlines()
line_number = 1
for line in lines:
     print(f"Line {line_number}: {line.strip()}")
     line_number += 1
 

'''
Output -
Line 1: PYTHON
Line 2: Program
Line 3: language
Line 4: python-version-1.0
Line 5: python3
'''