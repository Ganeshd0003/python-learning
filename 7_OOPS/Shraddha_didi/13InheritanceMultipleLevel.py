class A:
    varA = "Welocome to class A"

class B:
    varB = "Welocome to class B"
    
class C(A,B):
    varC = "Welocome to class C"
    
obj1 = C()
print(f"{obj1.varA}\n{obj1.varB}\n{obj1.varC}")