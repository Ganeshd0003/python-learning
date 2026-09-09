class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 

    @staticmethod  # IF we don't want to use self so we use staticmethod it is a decorator
    def hello():
        print("Hello Student")
    
s1 = Student("Ganesh",90)
s1.hello()   