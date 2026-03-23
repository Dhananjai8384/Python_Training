class Bird:
    def sound(self):
        print("Bird makes sound")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

b = Sparrow()
b.sound()