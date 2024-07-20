# calculate with constructor


class Cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

c1 = Cal(10,30)
print(c1.add())
print(c1.divide())
print(c1.multiply())
print(c1.sub())
