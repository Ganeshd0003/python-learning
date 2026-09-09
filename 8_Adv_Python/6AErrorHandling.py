while True:
    try:
        a = int(input("Enter the fist number : "))
        b = int(input("Enter the second number : "))
        print(f"Sum is {a+b}")
    except:
        print("Invalid Input!")