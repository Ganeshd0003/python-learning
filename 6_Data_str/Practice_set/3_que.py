# Start with numbers = [5, 2, 9, 1, 7] and do the following:

# Sort the list in ascending order.
# Append the number 10 to the list.
# Insert the number 100 to the 0th index.
# Remove the number 2 from the list.

numbers = [5, 2, 9, 1, 7]
print(numbers)

numbers.sort()
print(f"Sorted list {numbers}")

numbers.append(10)
print(numbers)

numbers.insert(0,100)
print(numbers)

numbers.remove(2)
print(numbers)


# extra methods tried
x  = numbers.copy()
print(x)

x.sort()
print(x)

x.append(100)
print(x)

yy = x.count(100)
print(yy)

x.extend(x)
print(x)