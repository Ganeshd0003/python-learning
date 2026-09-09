def hello():
    x = 100 # Local variable
    x = x + y
    print(x)
    print("hello")

y = 3 # global variable
print(y)
hello()

print("==============================================================")
# We can use it but cannot modify global variable in funtion, until
# calling --> global variable_name  ie. global a   -->(in this case)
def yoyo():
    print("Hello world!") 
    global a # This will tell to compiler MODIFY GLOBAL a
    a = 0

a = 5
print(a)
yoyo()
print(a) # Prints After modifiying through the fucntion 