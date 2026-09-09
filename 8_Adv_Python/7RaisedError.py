a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

if b == 0:
    raise ValueError("Please Don't divide by 0")

print(f"Division of {a} / {b} = {a/b}")