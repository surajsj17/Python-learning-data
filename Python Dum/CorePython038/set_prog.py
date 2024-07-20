# set : it's a collection of unique elements.set is mutable
#symbol -  {} 
#class - set()
s1 = {1,2,3,4,5,6,7,8,9,10,2,3,4,5}
print(s1)

s2 = {'monday','tuesday','wednesday'}
print(s2)
print(type(s2))

# empty set .. 
l1 = [] #  empty list
t1 = ()  # empty tuplr
s1 = {} #  empty dict
s3 = set() # empty set

#print(dir(set))

# add() : to add a single element to the set.
s3.add(10)
print(s3)

# update() : to add multiple elements to the set.
# multiple elements should be in the form of list or tuple.
s3.update([20,30,40,50,60])
print(s3)

s3.update({'python','java','java','c++'})
print(s3)

# remove() : to remove a single element from the set.
s3.remove('python')
print(s3)
#s3.remove('100') # KeyError: '100'

# discard() : to remove a single element from the set.
s3.discard('java')
s3.discard('100') # no error
print(s3)
#pop() : to remove a random element from the set.
s3.pop()
print(s3)

#union() : to get the union of two sets. merge two sets.
s1 = {"mon","tue","wed","thu"}
s2 = {"fri","sat","sun","mon","tue"}
s3 = s1.union(s2)
print(f"union using union() {s3}")
#or
s3 = s1 | s2
print("union using symbol |",s3)
#intersection() : to get the intersection of two sets.
#  returns common elements in both sets.
# & symbol
new_set = s1.intersection(s2)
print(f"intersection using intersection() {new_set}")
print(s1&s2)
# difference() :it's return uncommon elements of first set.
# - symbol
s1 = {"mon","tue","wed","thu"}
s2 = {"fri","sat","sun","mon","tue"}
print(s1-s2)
print(s1.difference(s2)) # {'thu', 'wed'}
# symmetric_difference() :
# returns uncommon elements of both sets.
print(s1.symmetric_difference(s2))
print(s1^s2)
# symmetric_difference_update() :
# update the set with symmetric difference(uncommon of both set).
s1.symmetric_difference_update(s2)
#  s1 = {"wed","thu","fri","sat","sun"}
print(s1)
# clear() : to remove all elements from the set.
# difference_update() : to remove common elements from the set.
s1 = {'a','b','c','d','e'}
s2 = {'c','d','e','f','g'}
s1.difference_update(s2) # {'a', 'b'}
print(s1) 
# intersection_update() : to remove uncommon elements from the set.
s1.intersection_update(s2) # {'c', 'd', 'e'}
print(s1)
# issuperset() : to check whether one set is superset of 
# another set or not.
s1 = {1,2,3,4,5,6}
s2  = {1,2,3}
print(s1.issuperset(s2)) # true
# issubset() : to check whether one set is subset of another set or not.
print(s2.issubset(s1)) # true

# isdisjoint() : to check whether two sets are disjoint or not.
s1 = {'a','b','c'}
s2 = {1,2,3,4,'d'}
print(s1.isdisjoint(s2)) # true


a = 10
b = 20


print("If you want to add two numbers, enter +")
print("If you want to subtract two numbers, enter -")
print("If you want to multiply two numbers, enter *")
msg = input(" Please enter your choice operator:")
if msg == '+':
    print(a+b)
elif msg == '-':
    print(a-b)
else:
    print("please enter valid operator.")