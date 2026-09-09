# some fuction operation

text = " i love Python programming "
# 1 remove extra space
print(text.strip())

# 2 convert to title case
print(text.title())

# 3 count how many time p appears
print(text.count("p"))

# check this is alphanumeric or not
text2 = "123abc"
print(text2.isalnum())

if text2.isalnum():
    print("yes it is alphanumeric")
else:
    print("No it is alphanumeric")