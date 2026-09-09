# Read the file and print all lines as a list using readlines()

with open("tasks.txt","r") as f:
    for line in f.readlines():
        print(line)