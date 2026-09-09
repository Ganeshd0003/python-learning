# Open notes.txt, read its content, and print it to the console.

try:
    f = open("notes.txt","r")
    content = f.read()
    print(content)
    f.close()
except Exception as e:
    print(e)