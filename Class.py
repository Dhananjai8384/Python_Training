class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("age:", self.age)

s1 = Student("Rahul", 20)
s1.display()