from abc import ABC, abstractmethod

# Abstract Base Class 
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def stop_engine(self):
        
        print("Engine stopped.")


class Car(Vehicle):
    def start_engine(self):
        print("Car starting") 


class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle starting") 


car = Car()
car.start_engine()
car.stop_engine()

motorcycle = Motorcycle()
motorcycle.start_engine()
motorcycle.stop_engine()
