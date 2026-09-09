# wap to keep asking the user to enter password until they enterd correct one

passs = "ganesh"

while True:
    password = input("Enter password\n")
    if password == passs:
        print("Correct Password")
        break
    else:
        print("Wrong Password! Please Enter correct password")