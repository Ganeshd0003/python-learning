# Enter number and get table of that number

table = int(input("Enter the number : "))

for i in range(1,11):
    print(f"{table} X {i:2d} = {table*i:2d}")