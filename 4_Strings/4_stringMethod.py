# Strings are immutable in Python (cannot be changed once created)
# In C and C++, strings can be mutable depending on how they are declared

name = "hello world"

# Attempting to change a character will raise an error
# name[0] = "A"  # ❌ Not allowed

# Get the length of the string
print("Length of name:", len(name))  # 11

print("=========================================")

# String case methods
print("Uppercase:", name.upper())        # "HELLO WORLD"
print("Lowercase:", name.lower())        # "hello world"
print("Title Case:", name.title())       # "Hello World"
print("Capitalize:", name.capitalize())  # "Hello world"
print("Swap Case:", name.swapcase())     # "hello world" -> "HELLO WORLD" (if letter is capital then it convet into small or vice versa)

print("=========================================")

# Removing whitespace
text = "   hello guys   "
print("Strip:", text.strip())    # Removes leading & trailing spaces -> "hello guys"
print("Left Strip:", text.lstrip())  # Removes leading spaces -> "hello guys   "
print("Right Strip:", text.rstrip()) # Removes trailing spaces -> "   hello guys"

print("=========================================")

# Finding and replacing text
text1 = "python is fun and fun and fun"

# Find the index of the first occurrence of a substring
print("Index of 'is':", text1.find("is"))  # 7

# Replace all occurrences of a substring
print("Replace 'fun' with 'awesome':", text1.replace("fun", "awesome"))
# Output: "python is awesome and awesome and awesome"

print("=========================================")

# Splitting and joining strings
text2 = "Apple,Banana,Pineapple"

# Split the string by comma
fruits = text2.split(",")
print("Split fruits:", fruits)  # ['Apple', 'Banana', 'Pineapple']

# Join the list back into a string with "-"
new_text = "-".join(fruits)
print("Joined fruits:", new_text)  # "Apple-Banana-Pineapple"

print("=========================================")

textt = "Python123"
print(textt.isalpha())
print(textt.isdigit())
print(textt.isalnum())
print(textt.isspace())
print(textt.isupper())
print(textt.islower())
print(textt.istitle())