# create a sting variable with your name and print first char, last char and length of the sting

name = str(input("Enter your name : "))

print(f"This is fist char of name {name[0:1]}")

print(f"This is last char of name {name[len(name)-1:]}")

print(f"This is length of name {len(name)}")