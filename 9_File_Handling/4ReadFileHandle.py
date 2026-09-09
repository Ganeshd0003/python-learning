# read file but file not found then program crash so use try except 

try:
    f = open("no_file.txt","r")
    
    content = f.read()
    
    print(content)
    
    f.close()
    
except FileNotFoundError:
    print("File not exists")