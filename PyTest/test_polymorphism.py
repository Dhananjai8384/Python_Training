class Bird:
    def sound(self):
        return "Bird makes sound"

class Sparrow(Bird):
    def sound(self):
        return "Sparrow chirps"

def test_polymorphism():
    b = Sparrow()
    assert b.sound() == "Sparrow chirps"