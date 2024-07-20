#regular expression

import re

# findall():

l = "Today we learn Python programming Python123 python is simple python programming"
x = re.findall("python",l)   # ['python', 'python']
y = re.findall(r'[pP]ython',l)   # ['Python', 'Python', 'python', 'python']

print(x)
print(y)

# search()

s = re.search ('python',l)
print(s)
print(s.span())  # (44,50)
print(s.group())  #python
print(s.start())  # 44
print(s.end())    # 55

#split() - same like split function in string

split1=re.split(' ',l)
print(split1)

#sub ()
replace = re.sub('python', 'java',l)
print (replace)

# make pattern string

data = "technology"
regex = '[olc]'
if re.search(regex,data):
    print("yes patter match")
else:
    print("no pattern match")
    
    
if re.match(regex,data):
    print("yes patter match")
else:
    print("no pattern match")
    
    