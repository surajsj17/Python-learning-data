#
class Parent1:
    surname = 'parmar' # atrribute
    def parent_method(self):
        print("I am parent  class method")
class Child(Parent1):
    name ='suvidha'
    def display_name(self):
        print("My name is",self.name,self.surname)

ch1 = Child()
ch1.display_name()

#ch1.parents()
ch1.surname = "patel"
ch1.display_name()
print(ch1.surname)
ch1.parent_method()


# multilevel inheritance

class grand_parent:
    surname = 'king'

class parent(grand_parent):
    m_name = 'steven'
    def display_name(self):
        print(f"my name is {self.m_name} {self.surname}")

class child(parent):
    def name(self,name):
        print(f"my name is{name} {self.m_name},{self.surname}")

ch = child()
ch.name('abc')



