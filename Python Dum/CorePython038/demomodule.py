# module is a python file which contains python code.
# how to load a module
# 2 ways:
# import module_name
# from module_name import function_name

import calc
print(calc.l1)
print(calc.addition(10,20))

from calc import square,l1
print(square(5))

# modules : 1. built-in modules 2. user-defined modules

# os module : it's provide a way of using operating system dependent functionality