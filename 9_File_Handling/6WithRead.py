with open("harry.txt") as f:
    content = f.read()
    print(content)
    # using with there is no need to f.close() with do it default
    
    # if we didn't give the f.close() means not close file it not thows error but it is good practice