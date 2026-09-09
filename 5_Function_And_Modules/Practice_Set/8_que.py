# Write sum_of_digits(n) that returns the sum of all digits of a given number.

n = int(input("Enter the number : "))

sum = 0

while n > 0:
    last = n % 10
    sum = sum + last
    n = n // 10

print(sum)
n = int(input("Enter the number : "))