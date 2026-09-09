# Create a tuple coordinates = (10, 20) and print both elements.
# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

coordinates = (10, 20)
print(coordinates)

# coordinates[0] = 50  #TypeError: 'tuple' object does not support item assignment

coordinates = list(coordinates)
print(coordinates)
print(type(coordinates))
coordinates[0] = 50
coordinates = tuple(coordinates) # this is illusion not actual tuple change, here another tuple created on another memory location (NOT ACTUAL)
print(coordinates)
print(type(coordinates))