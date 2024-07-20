# write the program to reverse the entered string

string = input("Enter the string :")
count = 1
reverse = (string[::-1])
for i in reverse:
     print(i,"index --> value = ",count)
     count+=1
     
'''
OUTPUT - 
Enter the string :python
n index --> value =  1
o index --> value =  2
h index --> value =  3
t index --> value =  4
y index --> value =  5
p index --> value =  6

'''