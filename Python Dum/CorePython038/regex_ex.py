import re # 1

text = 'abc 123 def 456 pqr 100  123456 !'
pattern = re.compile(r'\d\d\d') # or (r'\d{3}') create pattern [0-9][0-9][0-9]

print(r'old\new')
matches = re.search(pattern,text) # match or serach
print(matches)

f_all = re.findall(pattern,text)
print(f_all)

all = re.finditer(pattern,text)
print(all)

for m in all:
    print(m.group())



