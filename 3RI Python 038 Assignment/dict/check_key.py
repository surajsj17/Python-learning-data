#write the program to the check the key is exists or not

given_keys = input("Enter the keys : ")
dict1 = {'name':"suraj","last_name":"jaiswal","age":24}
for key in dict1.keys():
    if key == given_keys:
        print(dict1)
        print (" The key is already exists : ",given_keys)
        break
else:
    print(dict1)
    print("The key is not exists in dict  : ",given_keys)
    
'''
OUTPUT = Enter the keys : name
{'name': 'suraj', 'last_name': 'jaiswal', 'age': 24}
 The key is already exists :  name

Enter the keys : salary
{'name': 'suraj', 'last_name': 'jaiswal', 'age': 24}
The key is not exists in dict  :  salary

'''