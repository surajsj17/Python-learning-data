# write the program to print table of entered number 


num = int(input(" Enter the number :"))

counter = 1
sum = 0

while counter <= 10:
    sum = counter * num
    print (sum)
    counter += 1
    
    
'''
OUTPUT -
Enter the number :7
7
14
21
28
35
42
49
56
63
70
'''
