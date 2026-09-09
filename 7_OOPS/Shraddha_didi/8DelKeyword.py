class Student:
    def __init__(self,name):
        self.name = name
    
s1= Student("Ganesh")
print(s1.name)
del s1.name
print(s1.name) # Now the object has been deleted so it give error