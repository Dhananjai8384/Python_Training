from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def stop_engine(self):
        
        return "Engine stopped."

class Car(Vehicle):
    def start_engine(self):
        return "Car starting"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle starting"

def test_car():
    car = Car()
    assert car.start_engine() == "Car starting"
    assert car.stop_engine() == "Engine stopped."

def test_motorcycle():
    motorcycle = Motorcycle()
    assert motorcycle.start_engine() == "Motorcycle starting"
    assert motorcycle.stop_engine() == "Engine stopped."

