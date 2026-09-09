while True:
    try:
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        print(f"Sum of {a} + {b} = {a+b}")
        
    except Exception as e:
        print("Some error occurred! ",e)