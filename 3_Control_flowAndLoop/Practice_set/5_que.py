# Simple calculator: two numbers and operation selection

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operation = int(input("Choose operation:\n1: Add\n2: Subtract\n3: Multiply\n4: Division\n5: Modulo\n"))

match operation:
    case 1:
        print(f"Addition: {a} + {b} = {a + b}")
    case 2:
        print(f"Subtraction: {a} - {b} = {a - b}")
    case 3:
        print(f"Multiplication: {a} * {b} = {a * b}")
    case 4:
        print(f"Division: {a} / {b} = {a / b}")
    case 5:
        print(f"Modulo: {a} % {b} = {a % b}")
    case _:
        print("Invalid Input!")
