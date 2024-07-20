import pdb
print("hello")
print("we learn python")
total =0
#pdb.set_trace()
breakpoint()
for i in range(1,11):
    total = total + i
print(total)

#
assert 10 >0
#assert 5==0
assert 3<0, "3 is not less then 0"
# n = int(input("enter number:"))
# assert n > 0,'you enter wrong input'

def div(a,b):
    return(a/b)

pdb.set_trace()
print(div(10,5))
