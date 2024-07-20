# find the max number of list

list = [10,203,120,1030,10,111]
list1 = []
for i in list:
    if i not in list1:
        list1.append(i)
print (list1)
list1.sort()
print(list1)
print ()