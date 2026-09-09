# this code is same as 12InheritanceMultiLevel.py
# just the "brand" printed 
class Car:
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped.")
    
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type, brand):
        super().__init__(brand)
        self.type = type
        
car1 = Fortuner("Petrol", "Toyota")
car1.start()
print(f"{car1.type}\n{car1.brand}")
car1.stop()




# object introspction - it show all the method
print(dir(car1))