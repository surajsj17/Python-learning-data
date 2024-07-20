
# package : it's directory that contains a special file
#called __init__.py contain sub-packages or modules.

# from calculation_pkg import addition as ad
# print (ad.add1(10,40))

# import calculation_pkg as cal
# # from calculation_pkg import *
# print(cal.add1(10, 40))  # This should print 50
# print(cal.sub(40, 10))  # This should print 30


# # import pdb
# l1 = [10,20,30,45]
# total = 0
# # pdb.set_trace()
# breakpoint()
# for i in l1:
#     total = total + i
# print(total)

def add(a,b):
    return a+b
breakpoint()
print(add(20,30))
