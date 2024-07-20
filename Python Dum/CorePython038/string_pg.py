# string: sequence of characters enclosed in
# single quotes or double quotes or triple quotes.

a = 'python'

# type() : it is used to find the type of variable.
print(type(a))

# immutable : once we create a string object we can't modify.
# indexing : it is used to access the element of sequence.
s1 = "we learn python"

# index num start with 0 and end with n-1.
# slicing : it is used to access the subsequence of sequence.
# synatx: sequence_var[start_index:end_index:step]
# l 

print(s1[3])
print(s1[3:7])  # 3,4,5,6
print(s1[:9])
print(s1[::2]) # 1 step skip

print(s1[::-1]) # reverse the string
s = "python"
#negative indexing
print(s[::-1])  # nohtyp
# thon
print(s[2:6])
print(s[2:])

# noht
print(s[-1:-5:-1])
# + : it is used to concatenate the two strings.
s = "hello "
s1 = "world"
print(s+s1)

# * : it is used to repeat the string.
print(s*3)

s = "python is a programming language. it's easy to learn"
a = """ "python" programming """
print(a)

# membership operator : in, not in 
# print('p' in s)  # True
# print('hello' in s)  # False

# ch = input("enter a character:") # A 
# # aeiouAEIOU
# if ch in 'aeiouAEIOU':
#     print("vowel")
# else:
#     print("consonant")

# len() : it is used to find the length of sequence.
# s = "python"
# print(len(s)) # 6

#for loop
# count = 0
# for i in s: # i = p,y,t,h,o,n, ,p,r,o,g,r,a,m,m,i,n,g
#     count+=1
# print("length of string is :",count)


# for i in range(0,len(s)):
    #print(i)

# for  i in "hello":
# wap to find all character index number without using built in function.
# c = 0
# for i in s: # i = p,y,t,h,o,n
#     print(c,":",i)
#     c+=1
# dir() : it is used to find the all the methods of object.
print(dir(s))
# print(dir("h"))
# print(dir(str()))

# capitalize() : it is used to convert first character of string to uppercase.
s = "python is a programming language"
print(s.capitalize())
print("hello".capitalize())
new_str = "python".capitalize()
print(new_str)
print(s)

# casefold() : it is used to convert all the characters of string
# to lowercase.
print("HELOO WORLD".casefold()) # heloo world

# lower() : it is used to convert all the characters of string to lowercase.
print("HELLO WORLD GOOD morning".lower())

# title() : it is used to convert first character
# of each word to uppercase.

# upper() : it is used to convert all the characters of string to uppercase.

# swapcase() : it is used to convert all the uppercase characters to lowercase

#split() : it is used to split the string based on the given character.
s = "python,is,a,programming,language"
print(s.split(','))

# join() : it is used to join the sequence of strings.
l1 = ['python', 'is', 'a', 'programming', 'language']
print("|".join(l1))

# strip() : it is used to remove the leading and trailing spaces.
s = "    hello world     "
print(s.strip())

# Lstrip() : it is used to remove the leading spaces.
s1 = "#####hello world#####"
print(s1.lstrip('#'))
# Rstrip() : it is used to remove the trailing spaces.

# format() : it is used to format the string. placeholder {}
s = "hello {}".format("world")
print(s)
print("hello {} {} {}".format("world","good","morning"))
print("hello {2} {1} {0}".format("world","good","morning"))
print("hello {a} {b} {c}".format(a="world",b="good",c="morning"))
name = "suvidha"
l_name = "parmar"
print(f"hello my {name} is {l_name}")

print("my name is",name,"and last name is",l_name)
