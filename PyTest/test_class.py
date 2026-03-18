class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return f"Name:{self.name}, Age:{self.age}"
    
def test_display():
        s1 = Student("Rahul", 20)
        assert s1.display() == "Name:Rahul, Age:20"