class Student:                   # Student is class
    college_name = "ABC College" # class attribute

    def __init__(self,name,marks): # (__init__ is constructor) & self,name,age are parameters
        self.name = name         # name,age are attributes
        self.marks = marks
        print("adding new student in database...")

    def welcome(self):   # This is Method (normal Method)
        print("Welcome student,", self.name)

s1 = Student("Ganesh",90)
s1.welcome()
print(s1.name, s1.marks, s1.college_name)