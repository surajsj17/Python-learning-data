# write the program to entered the list from user and display the list in reverse order without using the reverse function

# There is 3 ways to do [slice,for loop,while loop]

# With slice operator
list_user = int(input("Enter the list element range :"))
list = []
for i in range(list_user):
    text=input("Enter the list element : ")
    if text.isdigit():
        list.append(int(text))
    else:
        list.append(text)
print (list)
print ("Reveres list "list[::-1])

'''
OUTPUT - Enter the list element range :5
Enter the list element : 1
Enter the list element : 2
Enter the list element : 3
Enter the list element : 4
Enter the list element : 5
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
'''

# # with for loop
list_user = int(input("Enter the list element range :"))
list = []
for i in range(list_user):
    text=input("Enter the list element : ")
    if text.isdigit():
        list.append(int(text))
    else:
        list.append(text)
print (list)
reverse_list = []
for r in range(len(list)-1,-1,-1):
    reverse_list.append(list[r])
print ("Reversed list = "reverse_list)

'''
OUTPUT - Enter the list element range :5
Enter the list element : 1
Enter the list element : 2
Enter the list element : 3
Enter the list element : 4
Enter the list element : 5
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
'''

# with while loop

list_user = int(input("Enter the list element range :"))
list = []
for i in range(list_user):
    text=input("Enter the list element : ")
    if text.isdigit():
        list.append(int(text))
    else:
        list.append(text)
print (list)
length = len(list)
counter = length
newlist = []
while counter > 0:
    newlist.append(list[counter -1])
    counter -=1
print ("The reversed List : "newlist)

'''
OUTPUT - Enter the list element range :3
Enter the list element : 1
Enter the list element : 2
Enter the list element : 3
[1, 2, 3]
[3, 2, 1]
'''