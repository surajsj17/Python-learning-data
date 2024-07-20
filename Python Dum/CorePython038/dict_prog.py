# Dictionary : {},ordered, mutable,  no duplicate keys

student_details = {'name': 'John', 'age': 25, 'course': 'Python'}

print(student_details,type(student_details))
# access elemets from dictionary using slicing operator.
print(student_details['name']) # john

# duplicate keys are not allowed
fruits = {'apple': 10, 'banana': 20, 'orange': 20,'apple': 40}
print(fruits) # {'apple': 40, 'banana': 20, 'orange': 30}

student_details['course'] = 'MDS'
print(student_details) # {'name': 'John', 'age': 25, 'course': 'MDS'}

#  can we list or tuple as key in dictionary?
# we can use tuple as key in dictionary but we can't use list as key in dictionary.

# empty dictionary {}
dict1 = {}
dict2 = dict()

#  dict of list
emp_details = {'name': ['John','alex','Ellena'],
                'age': [25,30,35],
                'course': ['Python','JAVA','Python']
                }

print(emp_details)
print(emp_details['name']) # ['John', 'alex', 'Ellena']
print(emp_details['name'][1]) # alex

# loops
fruits = {'apple': 10, 'banana': 20, 'orange': 20,'apple': 40}
# 1. loop through keys
for key in fruits:
    print(key)

# 2. loop through values
for k in fruits: # apple, banana, orange
    print(fruits[k])

print(fruits.keys()) # dict_keys(['apple', 'banana', 'orange']
# 3. loop through access key  using keys method.
for key in fruits.keys(): # [apple, banana, orange]
    print(key)
for value in fruits.values():  #[40, 20, 20]
    print(value)

for key,value in fruits.items(): # [('apple', 40), ('banana', 20), ('orange', 20)]
    print(key,value)

# how to update dictionary
car = {'brand': 'BMW', 'model': 'X5', 'year': 2020}
car['year'] = 2021
print(car)
car['color'] = 'red'

empty_dict = {}
empty_dict['name'] = 'John'
empty_dict['age'] = 25
empty_dict['course'] = 'Python'
print(empty_dict)

# update method : 
# update method is used to add multiple key value pairs to the dictionary.
# syntax: dict.update(key=value)
emp = {'name': 'John', 'age': 25}
# salary = {'salary': 50000}, {'location': 'Bangalore'}
emp.update(salary=50000, location='Bangalore')
emp.update({'dept': 'IT','hire_date': '2021-01-01','age': 30})

a = {'email':'john@123gmail.com','phone': 1234567890}

emp.update(a)

new_dict = emp.copy()
new_dict1 = emp
a = 30
b = a 

# get method :
d1 = {'a': 10, 'b': 20, 'c': 30}
print(d1['c']) # 30
print(d1.get('c')) # 30
# remove key value pair from dictionary
d1.pop('c')
print(d1) # {'a': 10, 'b': 20}
d1.pop('b')
#popitem method : remove last key value pair from dictionary
d2 = {'a': 10, 'b': 20, 'c': 30,'d': 40}
d2.popitem()
print(d2)
d2.popitem()
print(d2)
 # 'fromkeys',  'pop', 'popitem', 'setdefault', , 