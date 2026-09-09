# User only get essential information
class Car:
    def __init__(self,car_name):
        self.car_name = car_name
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def Start(self):
        self.acc = True
        self.brk = True
        self.cluth = False
        print(f"{self.car_name} car is started!")

c1 = Car("BMW")
c1.Start()