# set () function
# symbol {}
#class - set()

s1 = {1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5}
print (s1)

# empty set

s2 = set()
s2.add(1)  # single element to add
print(s2)

s2.update({10,20,30,40,50,60,"Monday"})   # multiple elements to add
print(s2)

s2.remove(10) # remove the single element
print(s2) 

s2.discard(100) # remove the single element but when you try to remove the element which not present in set --> no error

s2.pop()  # mostly it remove the first element in set
print(s2)

# s4 = {10, 20, 30, 40, 50, 60, 70, 80, 90}
# s3 = {40, 50}
# s4 = s4 - s3   #remove the multiple elements
# print(s4)

set1 = {"mon","tue","wed","thu"}
set2 = {"mon","tue","fri","sat"}

set3 =set1.union(set2)   #remove the elements from the set that are present in both sets 
print(set3)

set3 = set1 | set2    # 2nd way to union the elements
print(set3)

new_set = set1.intersection(set2)   # show the common elements
print(new_set)

set1 = {"mon","tue","wed","thu"}
set2 = {"mon","tue","fri","sat"}

set3 = set1.difference(set2)   # it will only show uncommon elements of the first set
print(set3)
set3 = set1-set2    # 2nd way 
print(set3)

set3 = set1.symmetric_difference(set2) # it will only show uncommon elements of the both sets
print(set3)
set3 = set1^set2
print(set3)

set1.symmetric_difference_update(set2)  #it will only show uncommon elements of the both sets but it change the first set elements
print(set1)

set1 ={1,2,3,4,5}
set2 ={1,2,3,6,7,8}
set1.difference_update(set2)  #it will only show uncommon elements of the first sets but it change the first set elements
print (set1)

s1 = {1,2,3,4,5}
s2= {1,2,3}
print(s1.issuperset(s2))  # it checks s2 elements are there in s1 then it will show true
print (s2.issubset(s1)) # it checks s2 elements are there in s1 then it will show true

s3 = {1,2,3,4,5}  # it checks s3 elements are there in s4 are not same element [true]
s4 = {'a', 'b'}

print(s3.isdisjoint(s4))