# Decorators: its's a function that takes another function 
# as parameter and extends the behavior of the latter function
# without explicitly modifying it.


# symbol : @ decorator_name
# its's function which is change the functionallity 
# of another function  by wrapping it.

# @ decorator_name
# def function_name():
#     pass
def smart_div(func): # outer function # func : div function div(5,10)
    def inner(a,b): # inner function  # div(5,10)
        if a<b:  # 5<10
            a,b = b,a # swap a and b # a = 10 b = 5
        return func(a,b)  # div(a,b)  # div (10,5)# 10/5 = 2.0
    return inner

@smart_div
def div(a,b):  # (5,10)
    return a/b

print(div(10,2)) # 5.0  # a = 10 b = 2

print(div(5,10)) # 5/10 = 0.5  # a = 5 b = 10
print(div(10,5)) #  10/5 =2.0

@smart_div
def sub(x,y):  # x = 10 y = 5
    return x-y # 10-5 = 5
print(sub(10,5)) # 5
print(sub(30,100)) # -70

# module : .py file (python file)  # collection of functions,class,object,variables
# package : collection of modules (folder) 
#it's include __init__.py file