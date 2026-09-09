while True:
    try:
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        print(f"Division of {a} / {b} = {a/b}")
        
    except ValueError:
        print("Please enter the number only")
        
    except ZeroDivisionError:
        print("Don't divide by zero")
    
    except Exception as e:
        print("Some error occurred! ",e)