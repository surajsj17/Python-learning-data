'''
Write a python program using class which contains two variables of 
type integer. Create and initialize the object using parameterized constructor.
Write a method to display maximum from given two numbers for all objects.
'''

class Max():
    def __init__(self,num,num1):
        self.num = num
        self.num1 = num1
    def check(cls):
         if cls.num > cls.num1:
            print ("The greater number : ",cls.num)
         else:
            print ("The greater number : ",cls.num1)
            
max_number = Max(10,20)
max_number1 = Max(90,20)

max_number.check()
max_number1.check()

'''
OUTPUT - The greater number :  20
         The greater number :  90
'''