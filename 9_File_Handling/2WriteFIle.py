# write a file ganesh.txt and inset some data

f = open("ganesh.txt","w")

string = "Ganesh is writing file via python\nThis is the second program in file i/o"

f.write(string)
f.close()