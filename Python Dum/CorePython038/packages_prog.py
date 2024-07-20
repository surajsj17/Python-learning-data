# package:  it's a directory that contains a special file 
# called __init__.py and contain sub-packages or modules.

# from calculation_pk import addition as ad
# print(ad.add1(10,20))



import calculation_pk as cal
print(cal.add2(10,20,30))


import calculation_pk.subtraction  as sb
print(sb.sub(10,20))


# Debugging: it's process of finding and 
#resolving defects or problems within a 
#computer program that prevent correct operation
# of computer software or a system.
# 1. pdb: python debugger
 # set_trace(): it's a function that can be used to set a breakpoint in the code.

# 2. breakpoint(): it's a function that can be used to set a breakpoint in the code.
import pdb
l1 = [10,20,30,40,50]
total = 0
#pdb.set_trace()
# breakpoint()
for i in l1:
    total = total+i
print(total)



def addition(a,b):
    return a-b

breakpoint()
print(addition(20,10))

# s : step into
# n: next
# c: continue
# q: quit



