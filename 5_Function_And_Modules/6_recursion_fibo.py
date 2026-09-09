# Here You consider series like 1,1,2,3,5,8...
# std format is 0,1,1,2,3,5,8...
def fibo(n):
    if (n == 0 or n== 1):
        return n
    return fibo(n-2) + fibo(n-1)

aaa = fibo(6)
print(aaa)