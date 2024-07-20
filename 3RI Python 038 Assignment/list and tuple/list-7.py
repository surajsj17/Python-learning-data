
# write the program and swapping 2 or 3 elements of list
list_user = int(input("Enter the list element range :"))
list = []
for i in range(list_user):
    integer=input("Enter the list element : ")
    if integer.isdigit():
        list.append(int(integer))
        if len(list) <= 3:
            pass
        else:
            print("Only 3 elements are allowed")
            exit()
    else:
       print ("Invalid list element")
       exit()
print (list)

length = len(list)
if length <= 2:
    list[0] , list[1] = list[1] , list[0]
if length <= 3:
    list[0],list[2] = list[2] , list[0]
print ("Rotation of list : ",list)

'''
OUTPUT - Enter the list element range :3
Enter the list element : 1
Enter the list element : 2
Enter the list element : 3
[1, 2, 3]
Rotation of list :  [3, 2, 1]
'''
    