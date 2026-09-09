# Write a program that writes three lines of text to a file tasks.txt

with open("tasks.txt","w+") as f:
    context = "hey how are you?\nI hope you are doing well\nOk bye..."
    f.write(context)
    f.seek(0)
    print(f.read())
    
    
# hey how are you?
# I hope you are doing well
# Ok bye...|<-------------------------------(cursor positon)

# when we write then the curosr goes at end and then we try to print the data but it prints blank line because the curosr at end
# so seek(0) is happed so curosr goes to starting point