# write the program and find the largest element in the list without using max functiona and take the input from user

list_user = int(input("Enter the list element range :"))
list = []
for i in range(list_user):
    integer=input("Enter the list element : ")
    if integer.isdigit():
        list.append(int(integer))
    else:
       print ("Invalid list element")
       exit()
print (list)
print()
remove_duplicates = []
for element in list:
    if element not in remove_duplicates:
        remove_duplicates.append(element)
print ("Checking the duplicate")
print(remove_duplicates)    
print()
length = len(remove_duplicates)
for value in remove_duplicates:
    if value > length:
        length = value
print ("Max number in list :",length)
        
'''
OUTPUT - Enter the list element range :5
Enter the list element : 1
Enter the list element : 2
Enter the list element : 222
Enter the list element : 33
Enter the list element : 1111
[1, 2, 222, 33, 1111]

Checking the duplicate
[1, 2, 222, 33, 1111]
Max number in list : 1111
'''