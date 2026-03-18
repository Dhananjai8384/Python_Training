class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

def test_inheritance():
    d = Dog()
    assert d.speak() == "Animal speaks"
    assert d.bark() == "Dog barks" 