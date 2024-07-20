#regular Expression
import re
# findall():
l = "Today we learn Python programming python123 python is simple python "
x = re.findall('python',l)
y = re.findall(r'[pP]ython',l)

print(y)
print(x) # []


#search()
s = re.search('python',l)
print(s)
print(s.span()) # index (15,21)
print(s.group()) # python
print(s.start()) # 15
print(s.end())

#split() : same like string split() method  s = "hello world" s.split(' ')
split1 = re.split(' ',l)
print(split1)

#sub: (replace string to another string)

replace = re.sub('python',"java",l)
print(replace)
print(l)
# make pattern and match it in given string '[]'
data = "technology"
regex = '[olc]' # make pattern use '[A-Z0-9a-z@]'  # '[A-Z]' --> '[]'
 # here we check col charcters present  any where in string c or o or l

# we can use two methods 1_search  and 2_ match
if re.search(regex,data):
    print("yes pattern match")
else:
    print("not match")



###############
if re.match(regex,data):
    print("yes pattern match")
else:
    print("not match")

name = 'python'

# python program to accept starting  with vowel.

regex = '^[IOaeiouAEU][a-zA-Z0-9_]*'  # a  # e_ # e123adASD

def check(string):
    if re.match(regex,string):
        print("Valid")
    else:
        print("invalid")

check("Amaya")

