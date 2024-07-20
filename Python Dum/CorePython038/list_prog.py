# List: mutable, ordered, indexed, duplicate are allowed.
# we can store any type of data.
# symbol : []
# class list: list()
l = [10,20,30,40,50] # int type list
l1 = ['python','java','c','c++'] # string type list
l2 = [10,20,30,40.67,50,'python','java','c','c++'] # mixed type list
# list of list 
l3 = [[10,20,30],[40,50,60,60,50],["c","c++","java"]]
print(l1)
print(type(l1))

# indexing : strat with 0 
# negative indexing : start with -1

l = [10,20,30,40,50]
#    0  1  2  3  4
#   -5 -4 -3 -2 -1
print(l[3]) # 40
print(l[-2]) # 40


print(l[:]) # [10,20,30,40,50]
print(l[2:])
print(l[1:4]) # 1,2,3 --> 20,30,40
print(l[::-1]) # reverse the list

l1 = ['python','java','c','c++'] # string type list
for i in l1:
    print(i)
#len() : it is used to find the length of sequence.
print(len(l1)) # 

for i in range(len(l1)): # 4 --> 0,1,2,3
    print(i)


#l3 =        [[10,20,30],[40,50,60,60,50],["c","c++","java",['a','b','c']]]
# indexing       0              1                 2
# inside_list = [10,20,30]
#                 0  1  2

# [40,50,60,60,50]
# 0,  1, 2, 3,  4

print(l3[2][1]) # c+

#mutable : we can change the value of list.
students_name = ['alex','john','smith','james']
#id() : it is used to find the memory location of variable.
# s = 'alex' --> a --> @
s = 'alex'

print("string s",id(s))
print("list students_name",id(students_name))
students_name[0] = 'alexander'
print(students_name)
print("after update list students_name",id(students_name))

#s[0] = 'A'
print(s)

s = "hello"
print(id(s))

s = "hello world " 
# hello --> hi
print(s.replace('hello','hi'))
print(s)

# dir() : it is used to find the list of methods and attributes of class.
print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# append : it is used to add the single element at the end of list.
l = [10,20,30,40,50]
# 100 --> add at the end of list.
l.append(100) # [10,20,30,40,50,100]
print(l)
l.append([200,300]) # [10,20,30,40,50,100,[200,300]]
print(l)

# extend : it is used to add the multiple elements at the end
# of list.
l = [1,2,3,4,5]
# 6,1,3,4
l.extend([6,1,3,4]) # [1,2,3,4,5,6,1,3,4]

# insert: it is used to add the element at the specific index.
l = ["java","c","c++","python"]
# l --> php at 2 index
l.insert(2,'php') # 1  # insert(index,element)
print(l)


# empty list
l = []
l1 = list()



s = "python programming" # 4
i =0
for char in s: # p,y,t,h,o,n  p,r,o,g,r,a,m,m,i,n,g    
   
    if char in "aeiouAEIOU": # o in "aeiouAEIOU"
       
        i = i+1    
print(i)



print("#"*50)
c= 0
for i in s: # p,y,t,h,o,n, ,p,r,o,g,r,a,m,m,i,n,g
    if  i in "aeiouAEIOU":
        c+=1
print(c)
#'clear': it is used to remove all the elements from list.
l = [1,2,3,4,5]
l.clear() # []
print(l) # []

# remove : it is used to remove the element from list.based on element(value)
l = [10,20,30,40,50]
l.remove(40)
print(l) # [10,20,30,50]
# 20 element remove from list.
# pop : it is used to remove the element from list based on index.
l.pop(1) # 20
print(l) # [10,30,50]
l.pop() # 50   # remove the last element from list.
print(l)

#'copy': it is used to create the copy of list.
l = [10,20,30,40,50]
new_list = l.copy()

 #'count': it is used to find the number of occurance of element in list.
student_name = ['alex','john','smith','alex','james','alex']
print(student_name.count('alex')) # 3

# 'index': its is used to find the index of element in list.
#syntax : list_name.index(element,start_index,end)
l = [10,20,30,40,50,10,20,30,40,50]
print(l.index(20)) # 1
print(l.index(20,2)) # 6  # 2  start reading from 2nd  index

#print(l.index("hello")) # ValueError: 'hello' is not in list,
#'reverse': it is used to reverse the list.
l = [10,20,30,40,50]
l.reverse() # [50,40,30,20,10]
print(l) # [50,40,30,20,10]
#'sort'
l = [20,50,30,40,10,60,5]
l.sort() # [5,10,20,30,40,50,60]
print(l) 
l = [20,50,30,40,10,60,5]
l.sort(reverse = True) # [60,50,40,30,20,10,5]
l = ['python','java','c','c++']
l.sort() # ['c', 'c++', 'java', 'python']
print(l)

# # how to take list element from user.
# n = int(input("how many element you want to add in list:"))  # 5
# l = [] # empty list
# for i in range(n): # 0,1,2,3,4  # range(1,n+1)
#     ele = input("Enter the element:") # '10' ,python
#     if ele.isdigit():  # "python".isdigit() --> False
#         ele = int(ele) # '10' --> 10
#         l.append(ele)  # [10,]
#     else:
#         l.append(ele) # 10,'python'
# print(l)

# str = "1234"
# # is digit : it is used to check the given string is digit or not.
# print(str.isdigit()) # True

# using split method
# l1 = input("Enter the element:").split()  # ' john alex smith' --> ['john','alex','smith']
# l2 = input("Enter the element:")  # '10 20 30 40 '
# l2 = l2.split()
# print(l1)
# print(l2)

# how to remove multiple elements from list.
l = [10,20,30,40,50]
remove_element = [20,30,50]
for i in remove_element: # i = 20,30,50
    l.remove(i)
print(l)

# how to remove multiple elements from list.
l = [10,20,30,40,50,20,30]
remove_element = [10,20,30,50]
copy_list = l.copy()
for i in copy_list: # i = 10,20,30,40,50  # L = [10,20,30,40,50]
    if i in remove_element:
        l.remove(i) # L = 20,30,40,50
print(" updated list:", l)

# + : it is used to add the two list.
l1 = [10,20,30]
l2 = [10,40,50]
print(l1 +l2) # [10,20,30,10,40,50]

# *  
l = [10,20]
print(l * 2) #[10,20,10,20]


