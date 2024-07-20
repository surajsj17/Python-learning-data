my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_list_number = []

# Reverse the list
for i in range(len(my_list) - 1, -1, -1):
    reverse_list_number.append(my_list[i])

# Iterate over the reversed list using enumerate to get both index and value
for index, value in enumerate(reverse_list_number):
    print("Index:", index, "Value:", value)
