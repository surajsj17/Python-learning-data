# name = input("Enter your name: ") # john
# course = input("Enter your course: ") # python

# print(name, course)
# print(name, course)


# a = int(input("Enter a number: ")) # 20
# b = int(input("Enter another number: ")) # 30 
# print(a + b) # 50


# a = int(input("Enter a number: ")) # 20
# b = int(input("Enter another number: ")) # 30 
# print(a + b) # 50

# a = int(input("Enter a number: ")) # 20
# b = int(input("Enter another number: ")) # 30 
# print(a + b) # 50


def add(a,b):
    return a+b

# print(add(20,50))
# print(add(300,200))
# print(add(1,4))

x = list(map(add,(2,3)))
print(x)