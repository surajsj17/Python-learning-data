# write the program to sorted the key of dictionary

dict1 = {"b": 2, "d": 3 , "c": 5, "a":7 }
dict1_key = {}

for key in sorted(dict1.keys()):
    dict1_key[key] = dict1[key]
print ("Original dictionary : ",dict1)    
print ("sorted the dictionary : ",dict1_key)

'''
OUTPUT - Original dictionary :  {'b': 2, 'd': 3, 'c': 5, 'a': 7}
         sorted the dictionary :  {'a': 7, 'b': 2, 'c': 5, 'd': 3}
'''

