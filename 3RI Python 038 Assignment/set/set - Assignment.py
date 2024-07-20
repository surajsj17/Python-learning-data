'''
Set Exersice:

Exercise 1: Add a list of elements to a set
L1 = [1,2,3,4]
S1 = {23,24,25}
o/p :S1 = {1,2,3,23,24,25}

'''
L1 = [1,2,3,4]
S1 = {23,24,25}
S1.update(L1)
print(S1)
'''
OUTPUT = {1, 2, 3, 4, 23, 24, 25}
'''
'''
Exercise 2: Return a new set of identical(common) items from two sets
s1 ={1,2,3,4,5}
S2  = { 1,2,3,4,6,7,8} 
o/p S3 = {1,2,3,4}
'''
s1 ={1,2,3,4,5}
S2  = { 1,2,3,4,6,7,8} 
s3 = s1.intersection(S2)
print(s3)

'''
OUTPUT = {1, 2, 3, 4}
'''
'''
Exercise 3: Get Only unique items from two sets.
s1 ={1,2,3,4,5}
S2  = { 1,2,3,4,6,7,8} 
o/p S3 = {5,6,7,8}
'''
s1 = {1,2,3,4,5}
S2  = { 1,2,3,4,6,7,8} 
s3=s1.symmetric_difference(S2)
print(s3)

'''
output - {5, 6, 7, 8}
'''
'''
Exercise 4: Update the first set with items that don’t exist in the second set.
s1 ={1,2,3,4,5}
S2  = { 1,2,3,4,6,7,8} 
o/p s1 = {5, 6, 7, 8}
'''
s1 ={1,2,3,4,5}
S2  = { 1,2,3,4,6,7,8} 
s1.symmetric_difference_update(S2)
print (s1)

'''
OUTPUT = {5, 6, 7, 8}
'''

'''
Exercise 5: Remove items from the set at once
            There is two ways to remove items from the set
'''
# 1 - way

set1 ={1,2,3,4,5,6,7}
set2  = {1,2,3,4} 
set1.difference_update(set2)
print (set1)

'''
OUTPUT = {5, 6, 7}
'''

# 2nd way
set1 ={1,2,3,4,5,6,7}
set2  = {1,2,3,4} 
set1= set1 - set2
print (set1)

'''
OUTPUT = {5, 6, 7}
'''

'''
Exercise 6: Return a set of elements present in Set A or B, but not both 
s1 = {1,2,3,9,7,8} 
s2 ={2,3,4,5,6,7,8,9}
o/p {1,4,5,6}
'''
s1 = {1,2,3,9,7,8} 
s2 ={2,3,4,5,6,7,8,9}
s3=s1.symmetric_difference(s2)
print (s3)
'''
OUTPUT - {1, 4, 5, 6}
'''

'''
Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
'''
s1 = {1,2,3,9,7,8} 
s2 ={2,3,4,5,6,7,8,9}
set3 = s1.intersection(s2)
print (set3)
'''
OUTPUT - {2, 3, 7, 8, 9}
'''

'''
Exercise 8: Update set1 by adding items from set2, except common items
'''
s1 = {1,2,3,9,7,8} 
s2 ={2,3,4,5,6,7,8,9}
s1 = s1.union(s2)
print (s1)
'''
OUTPUT - {1, 2, 3, 4, 5, 6, 7, 8, 9}
'''

'''
Exercise 9: Remove items from set1 that are not common to both set1 and set2
s1 = {1,2,3,9,78,46,90}
s2 ={2,3,4,5,6,7,8,9,7888,3333}
'''
s1 = {1,2,3,9,78,46,90} 
s2 ={2,3,4,5,6,7,8,9,7888,3333}

s1.intersection_update(s2)
print(s1)

'''
OUTPUT - {9, 2, 3}
'''