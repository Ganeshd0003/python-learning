table = []
for i in range(1,11):
    table.append(5*i)

print(table)


# insted of doing this, Short methond is list comprehension

table1 = [x*5 for x in range(1,11)]
print(table1)