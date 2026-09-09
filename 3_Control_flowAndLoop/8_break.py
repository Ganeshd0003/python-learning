a = int(input("Enter the number : "))
flag = 0
for i in range(2,a):
    if a%i==0 :
        flag = 1
        break
if a==1 :
    print("1 is neither odd nor prime")
elif flag==0 :
    print("Prime number")
elif flag==1 :
    print("Composite") 
else:
    print("Invalid input")