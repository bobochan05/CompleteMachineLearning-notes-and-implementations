#inheritance 
#inheritance is a fundamental concept in object oriented programming that involves creating new classes or subclasses or derived classes from superclass 
#superclass is the class from which other classes inherit properties and methods
#subclass is the class that inherits properties and methods from another class

class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting")
    def stop(self):
        print(f"{self.brand} {self.model} is stopping")

class car(vehicle):
        def __init__(self, brand, model, doors):
            super().__init__(brand,model)
            self.doors=doors

class bike(vehicle):
        def __init__(self,brand,model,type):
            super().__init__(brand,model)
            self.type=type

car1 = car("Mercedes", "S", 4)
bike1 = bike("Yamaha", "FZ", "Sport")
print(car1.__dict__)
print(bike1.__dict__)

