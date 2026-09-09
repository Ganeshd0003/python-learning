# use while loop to reverse give number

num = int(input("Enter the number : "))
reverse = 0
while num !=0:
    last = num % 10
    reverse = (reverse * 10) + last
    num = num // 10
print(f"The reversed number is {reverse}")


# OR
# this is for reverse string BUT we can also used it with typecasting
alpha = "abcd"
print(alpha[::-1])

number = 123456789
print(str(number)[::-1])