# Decorator function : It is used to change the functionality of the another function and take parameters and also wrapping it


def wrap(func):
    def innner(a,b):
        if a<b:
          a,b = b,a
        return(func(a,b))
    return innner


@wrap
def div(a,b):
    return a/b
print (div(10,20))
print (div(20,5))

@wrap
def sub(x,y):
    return x-y
print("sub",sub(10,20))
print("sub",sub(20,5))