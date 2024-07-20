# write the program and find the max and min key:value

dict1 = {"b": 2, "d": 3 , "c": 5, "a":7 }
max_key = " "
min_key = " "
min_value = len(dict1)
max_value = 0
for key,value in dict1.items():
        if value > max_value:
            max_value = value
            max_key = key
        if value < min_value:
           min_value = value
           min_key = key
print ("Original dictionary : ",dict1)
print("The max key : ", max_key ,max_value)
print("The min key : ", min_key ,min_value)

'''
OUTPUT: Original dictionary :  {'b': 2, 'd': 3, 'c': 5, 'a': 7}
The max key :  a 7
The min key :  b 2

'''