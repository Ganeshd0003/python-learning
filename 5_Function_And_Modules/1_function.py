a = 5
b = 6
c = 2

average = (a+b+c) / 3.0
print(average)

a = 99
b = 87
c = 94

average = (a+b+c) / 3.0
print(average)

# ==============================================

def average2(a,b,c):
    d = (a+b+c) / 3.0
    print(d)

average2(5,2,7)
average2(10,15,20)

# If i you want to store the average in another variable so
# it is not possilbe IN THIS CASE because, you just print the d ie.avg
# for that you need to USE return function
o1 = average2(1,2,3)
print(o1)  #so it prints NONE

# ==============================================

def average3(a,b,c):
    d = (a+b+c) / 3.0
    # print(d)
    return d

o2 = average3(100,200,300)
print(o2)