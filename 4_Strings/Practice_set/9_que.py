#check palandrome
a = str(input("Enter to check palandrome\n"))
if a == a[::-1]:
    print("Yes it is Palandrome")
else:
    print("No this is Not Palandrome")