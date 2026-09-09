a = 0
b = 1

for i in range(1,6):
    sum = a + b
    a = b
    b = sum
    
print(sum)