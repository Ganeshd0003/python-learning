class Student:                   # Student is class
    
    college_name = "ABC College" # class attribute
    
    def __init__(self,name,marks): # (__init__ is constructor) & self,name,age are parameters
        self.name = name         # name,age are attributes
        self.marks = marks
        print("adding new student in database...")
    
    
s1 = Student("Ganesh",21)       # s1, s2 are objects
print(f"Student Name : {s1.name}\nMarks : {s1.marks}\nCollege : {s1.college_name}")

s2 = Student("Rohit", 22)
print(s2.name, s2.marks,s2.college_name)