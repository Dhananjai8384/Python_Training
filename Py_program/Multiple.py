class Father:
    def skill(self):
        print("Driving")

class Mother:
    def skill1(self):
        print("Cooking")

class Child(Father, Mother):
    pass

obj = Child()
obj.skill()
obj.skill1()