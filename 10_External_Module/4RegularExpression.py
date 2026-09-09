# follow this documentaion : https://regexr.com/
import re

text = "The quick brown fox jumps over the lazy dog."

# search for the pattern
match = re.search("brown", text)
if match:
    print("match found!")
    print("Start index :",match.start())
    print("Start index :",match.end())
    
# find all occurances of the pattern
matches = re.findall("the", text, re.IGNORECASE)
print("Matches :",matches)

# replace the occurance of the pattern
new_text = re.sub("fox","cat",text)
print("New text :",new_text)
print("Old text :",text)
