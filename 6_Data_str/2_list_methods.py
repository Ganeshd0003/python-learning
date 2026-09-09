numbers = [1, 2, 3, 4, 5, 6, 7]
extra = [8, 9, 10]
print(numbers)

numbers.append(100)
print(numbers)

numbers.insert(0,10)
print(numbers)

numbers.pop()        # removes last element
print(numbers)

print(numbers.pop())  # removes *and prints* the removed element

numbers.append(122)
print(numbers)        # now you see the updated list

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)


numbers.extend(extra)

numbers.clear()
print(numbers)