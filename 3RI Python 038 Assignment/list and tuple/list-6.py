# write the program to take input from the input string and delete the word from the string

input_string = input("Enter a string: ")

string_to_delete = input("Enter substring to delete: ")

modified_string = input_string.replace(string_to_delete, "")

print(modified_string)

'''
OUTPUT - Enter a string: suraj jaiswal
Enter substring to delete: jaiswal
suraj 
'''