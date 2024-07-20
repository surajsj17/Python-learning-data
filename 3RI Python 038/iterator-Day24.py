# # An iterator is an object that contain a 
# #countable number of values.


# # to covert list into iterator we user iter() , __iter__()

# l1 =[10,20,30,40,50,60]

# itr = l1.__iter__()  # or itr = iter()
# print (type(itr))
# print (itr)

# print (itr.__next__()) # or itr=next()  10    
# print (itr.__next__())      #20
# print (itr.__next__())      #30


# print ("for loop")
# for i in itr:
#     if i == 50 :
#       print (i)
#       break
  
# print ("after the break")
# for i in itr:
#     print (i)
    

# class TopTen:
#     def __iter__(self):
#         return self
#     def __init__(self):
#         self.num = 1
#     def __next__(self):
#       if self.num <= 10:
#           value = self.num
#           self.num += 1
#           return value
#       else:
#           raise StopIteration
      
# itr = TopTen()      
# print (itr.__next__())
# print (itr.__next__())
# print ("*"*10)
# for i in itr:
#     print (i)
# print (itr.__next__())



# genetor = we write genetor in function 
# NOTE  - yield key word is used on be half of reture 

def power(max=0):
    n = 0
    while n < max:
      yield 2 ** n
      n += 1
p = power(5)

for i in p :
    print (i)    