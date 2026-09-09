# Palindrome without buit in 
s = str(input("Enter the string: "))

i = 0
j = len(s)-1
flag = True

while i<j:
    if s[i] != s[j]:
        flag = False
        break
    i+=1
    j-=1

if(flag==True):
    print("Palindrome")
else:
    print("NOt palindrome")