import copy
l1 = [[1,2,3],[4,5,6]]
l2  = copy.deepcopy(l1) # shallow copy
print("id l1:",id(l1))
print("id l2:",id(l2))

print("id of l1's 0 index':",id(l1[0]))
print("id of l2's 0 index':",id(l2[0]))

l1[0].append(200)
print(l1[0])
print(l2[0])

l1.append("hello")
print(l1)
print(l2)