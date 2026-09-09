from functools import reduce

number = []
for i in range(1,11):
    number.append(i)

print(number)

def sum(a,b):
    return a+b

c = reduce(sum, number)

print(c)