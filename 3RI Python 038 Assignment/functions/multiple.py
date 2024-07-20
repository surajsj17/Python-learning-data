# write the program to the mulitple to list by using function


list =[1,2,3,4,5]

def mul():
    counter = 1
    for i in list:
        counter *=i
    return counter
print("The multiple of element in list : ",mul())

'''
OUTPUT:
The multiple of element in list :  120
'''