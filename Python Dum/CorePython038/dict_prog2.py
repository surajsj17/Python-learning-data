# fromkeys(iterable,value): create a new dictionary with keys from sequence and values set to a value.
l1 = ['a', 'b', 'c', 'd']
v = 20
# {'a': 20, 'b': 20, 'c': 20, 'd': 20}
st_name = ['John', 'Doe', 'Smith']
course = "MDS"
new_dict = dict.fromkeys(st_name, course)
d = {}
d = d.fromkeys(l1, v)
print(new_dict)
print(d)

# setdefault method : its used to get the value of the key.
# If the key does not exist, it will add the key with the value.
# syntax: dict.setdefault(key,value). 
# value is optional. If value is not provided,
# it will set the value to None.
d1 = {'a': 10, 'b': 20, 'c': 30}
print(d1.setdefault('a')) # 10
print(d1.setdefault('d')) # None
print(d1.setdefault("name", "John"))
print(d1.setdefault("name", "Doe"))
print(d1) # {'a': 10, 'b': 20, 'c': 30, 'd': None, 'name': 'John'}

# wap to using two list (iterable)  create a dictionary.
names = ['John', 'Doe', 'Smith',]
course = ["MDS", "Python", "Java","c++"]
# o/p : {'John': 'MDS', 'Doe': 'Python', 'Smith': 'Java'}
# zip() : zip function is used to combine two lists.
print(zip(names, course))  # ('John', 'MDS'), ('Doe', 'Python'), ('Smith', 'Java')

print(dict(zip(names, course)))  # {'John': 'MDS', 'Doe': 'Python', 'Smith': 'Java'}


