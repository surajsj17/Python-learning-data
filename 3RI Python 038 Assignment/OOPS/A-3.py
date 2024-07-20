#Write a program to find the records of students having greater marks


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        greater_marks = 70
        if self.marks > greater_marks:
            print(f"Student Name: {self.name}, Marks: {self.marks}")
            print(f"The marks are greater : {self.marks}")

data = Student("Alice",85)
data.display()

'''
Output :
Student Name: Alice, Marks: 85
The marks are greater : 85

'''
        