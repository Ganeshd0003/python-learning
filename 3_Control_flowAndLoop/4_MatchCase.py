a = int(input("Enter the number between 1-10 "))

if(a>0 and a<11):
    match a:
        case 1:
            print("You won a charger")
        case 3:
            print("You won $30")
        case 7:
            print("You won a camera")
        case _: # default case
            print("Better luck Next time")
else:
    print("Invalid Input\nHint: Out of Range")