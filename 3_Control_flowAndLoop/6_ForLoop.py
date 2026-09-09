# Print 1 to 5 (each on a new line)
for i in range(1, 6):  # range 1 to end+1
    print(i)

print()
for i in range(4): # by default start form 0
    print(i)



# Print 1 to 10 on the same line
for i in range(1, 11):
    print(i, end=" ")


print("\n\n\nThis is table of 5")
for i in range(1, 11):
    print(f"\t5 X {i:2} = {5 * i:2}")


items = {'mango', 'apple', 'fig'}
for i in items:
    print(i)