# oops - object oriented programming languages
#class: it a blueprint of an object


class StudentDetails:
    stud_name = 'sky'
    stud_id = 1021
    def display(self):
        return f'The Student name is {self.stud_name} and ID is {self.stud_id}'
s1 = StudentDetails()
print (s1.display())    


class Car:
    name  = 'BMW'
    brand = 'indian'
    model_year = 2024
    def drive(self):
        return  f'{name} is moving '
    def display(self,color):
        return f'The car name is {self.name} the brand is {self.brand} and color is {color} and model is {self.model_year}'
 
x = 10
def display_():
     global x  
     x = 'hello'
     return x
print(x)
print(display_())
print(x)    