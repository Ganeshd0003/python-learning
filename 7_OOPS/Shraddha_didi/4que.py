# Create student class that takes name and marks of 3 subject as arguments in constuctor then create a method to print the average and create a thank you fuction and print it without self 

class Student:
    college = "VJTI"
    def __init__(self,name,sub1,sub2,sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.total = (sub1 + sub2 + sub3)/3
    
    def get_marks(self):
        print(f"\n{self.name} is studies in {self.college} and his score is {self.total}")
    
    @staticmethod
    def greet():
        print("Thank you!")

s1 = Student("Ganesh",100,90,80)
s1.get_marks()
s1.greet()


s2 = Student("Rohit",99,100,81)
s2.get_marks()
s2.greet()