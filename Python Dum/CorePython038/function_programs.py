# functions
# def function_name(parameters):
#     #return  statements

# display hello all msg using function

def msg():
    return 'hello all'

# call
print(msg())

# addition of two numbers
def add(a,b):
    return  a+b



# types of function arguments
# requiredfield(positional)
# named
print(add(b = 40, a=30))
# default
def emp_details1(name,dept,sal=35000):
    return f"my name is {name} and i 'm working in {dept}.my sal is {sal}"


print(emp_details1('suvidha','IT'))
print(emp_details1('amaya','IT',45000))
# variable length (*args)
# N NUMBERS SUM
def addition(*args): # iterables [list,tuple]
    total =0
    for i in args:
        total+=i
    return total 

print(addition(20,30,40))
print(addition(1,2,3,4,5))
print(addition(*[12,13,14,15,16]))
print(addition(30,40))


# key variable length (**kwargs) : dictionary
# emp_details(name='suvidha',dept='IT',sal=45000)
# emp_details(name='amaya',dept='IT')
#emp_details(name='amaya',sal=45000,dept='IT',exp=2,loc='pune')
#emp_details(**{'name':'amaya','sal':45000,'dept':'IT','exp':2,'loc':'pune'}
def emp_details(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} is : {v}")
  


emp_details(name='suvidha',dept='IT',sal=45000)
print("#"*50)
emp_details(name='amaya',dept='IT')
print("#"*50)
emp_details(name='amaya',sal=45000,dept='IT',exp=2,loc='pune')#emp_details(**{'name':'amaya','sal':45000,'dept':'IT','exp':2,'loc':'pune'}
print("#"*50)
d1 = {'name':'amaya','sal':45000,'dept':'IT','exp':2,'loc':'pune','job':'developer'}
emp_details(**d1)
