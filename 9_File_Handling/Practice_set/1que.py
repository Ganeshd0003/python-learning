# Create a text file notes.txt using Python and write "Learning Python is fun!" into it

f = open("notes.txt","w")

context = "Learning Python is fun!"

f.write(context)

print(context)

f.close()