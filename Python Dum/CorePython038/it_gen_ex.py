#  find power of 2
# using iterator

class Powtwo:
    def __init__(self,m): # 5
        self.n = 0 # n=0
        self.m =m

    def __iter__(self):
        return  self
    def __next__(self):
        if self.n  > self.m: # m =5  n>m 0>5 ,1>5,2>5,5>5-->stop
            raise  StopIteration
        r =  2 ** self.n # 1 2 ^1 -->2 ,2 ,2^2
        self.n +=1
        return  r # 1st 1,

x = Powtwo(5)
# print(x.__next__()) # 2^0 # 1
# print(x.__next__()) # 2^1 #2
# print(x.__next__()) # 2 ^2 #4
# print(x.__next__()) # 2^3
# print(x.__next__()) # 2^4
# print(x.__next__()) # 2^5
#print(x.__next__()) # 2^6 # error
# print("#"*30)
for i in x:
    print(i)
print("*"* 30)

#
def powtwgen(max=0): # 5 # 2^0,2^1,2^2,2^3,2^4
    n=0
    while n < max:
        yield 2 **n # iter()
        n+=1

#
g = powtwgen(5)
print(next(g)) #2^0 =1
print(next(g)) # 2^1 =2
for i in g:
    print(i)


