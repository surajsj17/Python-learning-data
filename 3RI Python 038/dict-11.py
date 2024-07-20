# dict Type:
# ----------
# --> It is a sequence data type, it able to store sequence of elements in
# the form of Key-Value pairs.
# --> To represent elements in dict data type we will use the following
# pattern.
# {Key1:Val1, Key2:Val2,....Key-n:Val-n}
# no duplicate keys

student_details ={"name":"Sumit","age":26,"courses":["python","AWS"]}
print (student_details)
print (student_details['courses'][1])
print(dir(dict))

# duplicate keys are not allowed
fruits ={'apple':10, 'orange':20, 'apple':30}
print (fruits)
#{'apple': 30, 'orange': 20}

# we can use tuple as key in dictionary but we can't use list in dictionary as key 

dict = {}


fruits = {'apple':10, 'orange':20, 'mango':30}
for i in fruits:
    print(i)
    
# apple
# orange
# mango

for i in fruits:
    print(fruits[i])
    
# 10
# 20
# 30

emp_details = {'name': ['smith',"jenny"],
               'age': [24,45,32],
               'gender': ['male','female']}
print(emp_details)
print(emp_details['name'])
print(emp_details['age'][1])

for i in emp_details:
    print(emp_details[i][1])
    
'''
output - jenny
         45
         female
'''

#keys()
fruits = {'apple':10, 'orange':20, 'mango':30}
for key in fruits.keys():
     print(key ,end = " ")
# output = apple orange mango

#values()
for value in fruits.values():
     print(value ,end = " ")
# output = 10 20 30 

#items()
for items in fruits.items():
    print(items ,end = " ")
    print()
# output - ('apple', 10) ('orange', 20) ('mango', 30) 

# how to update dictionary
car = {'brand':"BMW","price":10000,"colour":"black"}
car["colour"] = "red"
print(car) # {'brand': 'BMW', 'price': 10000, 'colour': 'red'}
car["size"] = [2,4]  
print (car)  #{'brand': 'BMW', 'price': 10000, 'colour': 'red', 'size': [2, 4]}


#update method
emp_details = {"emp_name":"sumith", "emp_id":101}
emp_details.update(emp_name="pradeep")
print(emp_details) #{'emp_name': 'pradeep', 'emp_id': 101}
emp_details.update({"dept":"IT","salary":10000})
print(emp_details) #{'emp_name': 'pradeep', 'emp_id': 101, 'dept': 'IT', 'salary': 10000}

#margin to dict

emp_details_new = emp_details.copy()
print(emp_details_new) #{'emp_name': 'pradeep', 'emp_id': 101, 'dept': 'IT', 'salary': 10000}

# 2nd way

# emp_details_new = dict(emp_details)
# print(emp_details_new) #{'emp_name': 'pradeep', 'emp_id': 101, 'dept': 'IT', 'salary': 10000}  


# get method
d1 = {'a':10,'b':20,'c':30}
print (d1.get('a')) #10

# remove the dict 
d1.pop('c')
print(d1) #{'a': 10, 'b': 20}

# remove the dict popitems
d1.popitem()
print(d1) #{'a': 10}


#fromkey (iterable,value): create a dictionary with keys from single value

name = ["pradeep","akash","sumeth","suraj"]
course = "Python"
new_name = dict.fromkeys(name,course)
print(new_name) 

#setdefault method : its used to get the value of the key
#if the key does not exist,it will add the key with the value
d1 = {"a":1,"b":2,"c":3,"d":4}
print (d1.setdefault("a"))  #1
print (d1.setdefault("e"))  # None
print (d1.setdefault("name","john")) #john
print (d1.setdefault("name","sam"))  #john
print (d1)

'''
1
None
john
john
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': None, 'name': 'john'}
'''
#  combination of 2 list and create dict by useing zip()

name1 = ['pradeep','akash','sumath','suraj']
course1 = "python","java","c++","AWS"
print(zip(name1,course1))
# print(dict(zip(name1,course1)))
#{'pradeep': 'python', 'akash': 'java', 'sumath': 'c++', 'suraj': 'c++'}