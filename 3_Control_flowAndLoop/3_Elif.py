age = int(input("Enter you age : "))

if(age>0 and age<=100):
    if(age>18):
        print("You Can Drive")
    elif(age==18):
        print("Go and Apply for Licence")
    else:
        print("You Cannot Drive")

print("End of program")