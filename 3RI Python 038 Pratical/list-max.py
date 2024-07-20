# find the max number of list

list = [10,203,120,1030,10,111]
print (list)
counter = 0
for i in list:
    if i > counter:
        counter = i
print ("The max number : " ,counter)    
    
print ("*" * 50)  
    
# USING APPEND FUNCTION     
list = [10,203,120,1030,10,111]
list1 = []
for i in list:    
    if i not in list1:
        list1.append(i)
print ("Original list : ",list1)
list1.sort()
print("Sorted list : ",list1)
max_number = list1[-1]
print("The max number in give list : ",max_number)
print("The 2nd max number in give list : ",list1[-2])
print ("The minimum number in give list : ",list1[0])


print ("*" * 40)

list = [10,203,120,1030,10,111]
print (list)
length = list[0]
for i in list:
    if i < length:
        length = i
print ("The minimun number : " ,length)    


