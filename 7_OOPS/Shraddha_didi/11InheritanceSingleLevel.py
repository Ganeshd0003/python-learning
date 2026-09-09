class Car:
    colour = "White"
    
    @staticmethod
    def start():
        print("Engine Started...")
    
    @staticmethod
    def stop():
        print("Engine Stopped...")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
print(car1.colour,car1.name)