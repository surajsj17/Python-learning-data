# LIST DATA STRUCTURE []
'''
- If we want represent group of individual object as a single entity where insertion order preserved
  and duplicates are allowed,then we should go for List
- List is Mutable
- insertion order preserved
- duplicates objects are allowed
- heterogeneous objects are allowed (multiple datatypes are allowed)
- Python support both positive and negative indexes
- slice operations are allowed
- Example -  
            list = [10,20,"python",1.5] ---> heterogeneous list
'''

list = [10,20,"python",1.5]
print (list)
print (type(list))   # type is used to check the datatype
print (id(list))     # ID is used to check the storage ID



# With dynamic input

list = eval(input("Enter the list: ")) # NOTE - put input in this way(use bracket)  = [1,2,3]
print(list)
print (type(list)) # type is used to check
'''
OUTPUT = Enter the list: [1,2,3]
         [1, 2, 3]
         <class 'list'>
'''
# With list() function

l = list(range(2,10,2)) #We can use range function in list
print(l)
'''
OUTPUT = [2, 4, 6, 8]
'''

# We can covert string to list by using list() function -- 1 way

string = "3Ri Tech"
l=(list(string))
print(l)

'''
OUTPUT = ['3', 'R', 'i', ' ', 'T', 'e', 'c', 'h']  # It will take single character as single object in list
'''
# we can convert string to list by using split() function -- 2 way

string = "3Ri Tech"
l=string.split()
print(l)

'''
OUTPUT = ['3Ri', 'Tech']
'''


# Indexing in list

list = [1,2,3,4,5,6,7]
print ([0])
print (list[4])
print ("negative =",list[-1])
'''
OUTPUT = [0]
          5
         negative = 7
'''
# Nested lists 

nested_list = [[10,20,30,40,50],["python","programming",["a","b","c"]]]
print (nested_list)             # print nested list
print (nested_list[1][2][1])    # need to print " b " letter

'''
OUTPUT = [[10, 20, 30, 40, 50], ['python', 'programming', ['a', 'b', 'c']]]
         b
'''

# Slice operator in list.
# [start, end, step]  -- > format

list = [1,2,3,4,5,6,7,8,9,10]
print (list[0:5])
print (list[0:5:2])
print (list[0:10:2])
print (list[0:10:3])  
print (list[::-1]) # reverse list 
print (list[0:1000])  # end value is out of range but it will not show errors in list it display all list elements still end

'''
OUTPUT = [1, 2, 3, 4, 5, 6, 7]
         [1, 3, 5]
         [1, 3, 5, 7, 9]
         [1, 4, 7, 10]
         [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
# LIST is Mutable

list = [1,2,3,4,5]
print (list)
list[3]=777  # adding the element through index value 3 = 777
print (list)
'''
OUTPUT = [1, 2, 3, 4, 5]
         [1, 2, 3, 777, 5]
'''

list = [1,2,3,4,5]
print (list)
list[3:3]= 888,222  # adding the 2-element through index value 3 = 888,222
print (list)

'''
OUTPUT = [1, 2, 3, 4, 5]
         [1, 2, 3, 888, 222, 4, 5]
'''

# IMPORTANT IN-BUILD FUNCTIONS IN LIST
'''
1 - list()
2 - .split()
3 -.append()
4 -.extend()
5 -.insert()
6 -.remove()
7 -.pop()
8 -.sort()
9 -.reverse()
10 -.count()
11 -.copy()
12 -.len()
13 -.index()
'''

# list ()

string = "3Ri Tech"
l=(list(string))
print(l)

'''
OUTPUT = ['3', 'R', 'i', ' ', 'T', 'e', 'c', 'h']  # It will take single character as single object in list
'''
# .split()

string = "3Ri Tech"
l=string.split()
print(l)

'''
OUTPUT = ['3Ri', 'Tech']
'''

# . append() is used to add the object to the end of the list

list = [1,2,3,4,5]
print (list)
list.append(6)  # append the element 6 in list
print (list)

'''
OUTPUT = [1, 2, 3, 4, 5]
         [1, 2, 3, 4, 5, 6]

'''
# .extend() - add one list of elements to other list

list = [1,2,3,4]
print (list)
list2 = [5,6,7]
list.extend(list2)  # In list2 elements are added to list
print(list)

'''
OUTPUT - [1, 2, 3, 4]
         [1, 2, 3, 4, 5, 6, 7]
'''

# .insert() is used to insert a new element at the given index value to next element


list = [1,2,3,4]
print (list)
list.insert(2,400)
print(list)

'''
OUTPUT = [1, 2, 3, 4]
         [1, 2, 400, 3, 4]
'''

# .remove() it will remove the given element in list

list = [1,2,3,4]
print (list)
list.remove(2)
print(list)


'''
OUTPUT = [1, 2, 3, 4]
         [1, 3, 4]
'''

# pop() it will pop (remove) the given index value other wise it will remove the last element

list = [1,2,3,4]
print (list)
list.pop(1)
print(list)

'''
OUTPUT = [1,2,3,4]
         [1, 3, 4]
'''

# .sort() is used to sort the elements of a list

list = [1,3,2,4,6,9]
print (list)
list.sort()
print(list)

'''
OUTPUT = [1, 3, 2, 4, 6, 9]
         [1, 2, 3, 4, 6, 9]
'''

# sort() in descending order
list = [10,20,30,40,20,30]
list.sort(reverse=True)
print (list)
'''
OUTPUT = [40, 30, 30, 20, 20, 10]   
'''

#.reverse() it will reverse the element in the list

list = [1,2,3,4,5,6,7,8,9,10]
print (list)
list.reverse()
print(list)
'''
OUTPUT = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
         [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''
#.count() -> it will count the elements in list

list = [1,2,1,1,2,2,3,4,5,6]
print(list.count(1))
print(list.count(2))

'''
OUTPUT = 3
         3
'''

# copy() its will copy the elements to another list

list = [1,2,3,4,5]
list1= []
list1=list.copy()
print (list1)

'''
OUTPUT = [1, 2, 3, 4, 5]
'''
# len() is will to check the length of the list

list = [1,2,3,4,5]
list1=len(list)
print ("The length of list = ",list1)

'''
 OUTPUT = The len of list =  5
'''

'''
LOOPS 
1 - List with for and while loops
'''
# simple for loop example

list = [1,2,3,4,5]
for i in range(len(list)):
    print (list[i] ,end= " ")
    
'''
OUTPUT - 1 2 3 4 5
'''
# simple while loop example

list = [1,2,3,4,5]
counter = 0
while counter < len(list):
    print (list[counter] ,end= " ")
    counter += 1

'''
OUTPUT - 1 2 3 4 5 
'''

# display the elements of list index wise

list = ["A","B","C","D","E","F","G","H","I"]
l=len(list)
for i in range(l):
    print (f"{list[i]} is available at positive index : {i} and at negative index : {i-l}" )

'''
OUTPUT = A is available at positive index : 0 and at negative index : -9
         B is available at positive index : 1 and at negative index : -8
         C is available at positive index : 2 and at negative index : -7
         D is available at positive index : 3 and at negative index : -6
         E is available at positive index : 4 and at negative index : -5
         F is available at positive index : 5 and at negative index : -4
         G is available at positive index : 6 and at negative index : -3
         H is available at positive index : 7 and at negative index : -2
         I is available at positive index : 8 and at negative index : -1
'''

# index() function is used for checking the index value

list = [10,20,30,40,20,30]
print(list.index(20,2))  # start,end,value

'''
OUTPUT = 4
'''

'''
 - USING MATHEMATICAL OPERATORS FOR LIST OBJECT
    1 - Concatenation operator (+)
    2 - Repetition operator (*)
-  COMPARING LIST OBJECTS
-  MEMBERSHIPS OPERATORS
'''

# Concatenation operator

list = [1,2,3,4,5]
list2 =[6,7,8,9]
result = list + list2
print (result)

'''
OUTPUT = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
# repetition operator

list = [1,2,3,4,5]
result = list * 3
print (result)

'''
OUTPUT = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
'''

# Comparing operator

list = [1,2,3,4,5]
list2 =[1,2,3,4,5]
list3 =[4,2,7,8,9]

print (list == list2)   # true
print (list == list3)   # false
print (list2 != list3)  # true
print (list <= list3)   # true
print (list >= list2)   # true

'''
OUTPUT =    True
            False
            True
            True
            True
'''

# - in operator
# - not in operator

list = [10,20,30,40,50,60]
print (10 in list)        #true
print (20 not in list)    #false
print (30 in list)        #true
print (50 not in list)    #false

'''
OUTPUT = True
         False
         True
         False
'''

# Take input from user for the list

list = int(input("Enter the list : "))   # len of list
new_list =[]

for i in range(list):
    element = input("Enter the element : ")
    if element.isdigit():                      #check the int value
        new_list.append(int(element))
    else:
        new_list.append(element)
print(new_list)

'''
OUTPUT - Enter the list : 5
Enter the element : 1,2,3,suraj
Enter the element : 1
Enter the element : 2
Enter the element : 3
Enter the element : 4
['1,2,3,suraj', 1, 2, 3, 4]
'''

# remove the duplicates elements for lists 
l = [10,20,30,70,50,20,70,20,90,]
remove_element =[20,70]
copy_list = l.copy()
for i in copy_list:
    if i in remove_element:
        l.remove(i)
print ("Updated List : ",l)

'''
OUTPUT - Updated List :  [10, 30, 50, 90]

'''

