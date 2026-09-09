a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

try:
    c = a/b
    print(c)
    
except Exception as e:
    print(e)
    

finally:
    print("This always printed either condion is T or F")