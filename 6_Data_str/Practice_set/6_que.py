# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)
# Add 5 to the set, remove 2, and check if 4 is in the set.
# Create two sets:
# a = {1, 2, 3}
# b = {3, 4, 5}
# Find their:
# Union
# Intersection
# Difference (a - b)

my_set = {1, 2, 3, 3, 4}
print(my_set) # set not allow duplicacy so 3 will removed

my_set.add(5)
print(my_set)

my_set.discard(2)
print(my_set)

print("\n"*2)
a = {1,2,3}
b = {3,4,5}

print(a.union(b))
print(a.intersection(b))
print(a.union(b))