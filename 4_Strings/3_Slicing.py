# String slicing means taking a part (substring) from a string using index ranges.

name = "ganesh"
print(len(name))
print(name[0:3])

print("\n"*3)

print(name[0:-2]) # Trick : string size is 6 so (6 -3) so it makes [0:4]

print(f"\t{name[:6]}")  #Replace first empty space as 0 
print(f"\t{name[0:]}")  #Replace second empty space as length ie. 6 (in this case) 
print(f"\t{name[:]}")   #replace fist as 0 and second as length

# skip character ie. n-1
a = "abcdefg123456"
print(len(a))

print(a[0:13:1]) #so n-1 ie. 1-1 = 0 , 0 char skip after each exection
print(a[0:13:3]) #so n-1 ie. 3-1 = 2 , 2 char skip after each exection