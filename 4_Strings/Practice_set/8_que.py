# Count how many vowels in string

text = "A Coding in Python is fun"

vowels = "aeiouAEIOU"
count = 0
for i in text:
    if i in vowels:
        count+=1

print(f"{count} are vowels in string")