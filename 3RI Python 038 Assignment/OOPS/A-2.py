'''
Write a program to perform all the arithmetic operations between two numbers
'''


class Arithmetic():
    def __init__(self,num,num1):
        self.num = num
        self.num1 = num1
    def add(self):
        result = 0
        result = self.num + self.num1
        print ("Add : ",result)
    def sub(self):
        result = 0
        result = self.num - self.num1
        print ("Sub : ",result)
    def mul(self):
        result = 0
        result = self.num * self.num1
        print ("mul : ",result)
    def div(self):
        result = 0
        result = self.num / self.num1
        print ("div : ",result)


add1 = Arithmetic(10,30)
add1.add()
        
sub1 = Arithmetic(40,20)
sub1.sub()

mul1 = Arithmetic(10,10)
mul1.mul()

div1 = Arithmetic(40,5)
div1.div()        

'''
OUTPUT - 
Add :  40
Sub :  20
mul :  100
div :  8.0
'''