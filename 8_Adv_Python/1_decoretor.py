def decorator(func):
    def wrapper():
        print("This is before execution")
        func()
        print("This is after execution")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()