#pdb
import pdb

total =0
#pdb.set_trace()
for i in [1,2,3,4,5]:
    total = total+ i
print(total)



# n : execute current line and move your cursor to next line
# s : step in
# c: continue

def add(a,b):
    print(a+b)
pdb.set_trace()
add(20,30)