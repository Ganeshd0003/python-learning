marks = {"harry":34,"jack":43,"lily":90}

print(marks,type(marks))

print(marks["lily"])

marks["harry"] = 100 

print(marks)

print("\n"*2)
print(marks.keys())
print(marks.values())
print(marks.items())
print("\n"*2)

marks.pop("lily")
print(marks)

marks.clear()
print(marks)