# An iterator is an object that contains a
# countable number of values.

#function called __init__(),
# which allows you to do some initializing
# when the object is being created.


l1 = [1,2,3,4,5,6,7,8,9,10]
for i in l1:
    print(i)
print("Hello"* 3)

for i in l1:
    print(i)
print("Hello"* 3)
# List : Fully stored in memory
# for i in list(range(10000000000000000000)):
#     print(i)

#iter()
# x = iter(range(1000000000))
# for i in x:
#     if i == 100:
#         break
#     print(i)
# for i in x:
#     if i == 200:
#         break
#     print(i)
# to covert list into iterator we user iter() ,__iter__()
 # l1 --> iterator
itr = l1.__iter__()  #or itr = iter(l1)
print(type(itr))
print(itr)
# next() or __next__()
print(itr.__next__()) # 1 print(next(itr)
print(itr.__next__())  # 2
print("hellloooooo")
# print(type(itr))
for i in itr:  #
    print(i) # 3
print("#"*1000)
print("done")

print(l1[0])
print(l1[1])
for i in itr:
    print(i)

print("#"*100)
for i in itr:
    print(i)


class TopTen:
    def __iter__(self): #  return object
        return self
    def __init__(self):
        self.num = 1
    def __next__(self): # element return
        if self.num<=10:
            val=self.num
            #print("val:",val)
            self.num+=1
            #print("num:",self.num)
            return val # current value
        else:
            raise StopIteration # Exception
print("______________________________________________________________")
values=TopTen()
print(values.__next__()) #1
print(values.__next__()) #2
print("______________________________________")
for i in values:
    print(i)
print(values.__next__())

for i in values:
    print(i)