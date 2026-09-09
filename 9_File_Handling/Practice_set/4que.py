# Open tasks.txt in append mode and add a new line "Task Completed!".

with open("tasks.txt","a+") as f:
    context = "\nTask Completed"
    f.write(context)
    f.seek(0)
    print(f.read())