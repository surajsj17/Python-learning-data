# write the program to accept the input list from the user and display the alternative elements


list_input = int(input("Enter the range of elements in the list : "))
list = []
for i in range(list_input):
    text = input("Enter the list element : ")
    if text.isdigit():
        list.append(int(text))
    else:
        list.append(text)
print(list[::2])

'''
OUTPUT:  Enter the range of elements in the list : 6
Enter the list element : 1
Enter the list element : 2
Enter the list element : 3
Enter the list element : suraj
Enter the list element : b
Enter the list element : q
[1, 3, 'b']

'''