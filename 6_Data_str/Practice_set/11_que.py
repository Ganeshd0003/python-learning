# Write a program that merges two dictionaries into one.

dict1 = {"a": 1, "b": 2, "z": 99}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}
print(merged)