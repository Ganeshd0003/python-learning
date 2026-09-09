def repeat(n):
    def decorator(func):
        def wrapper(a):
            for _ in range(n):
                print("This is before exection...")
                func(a)
                print("This is after exection....\n")
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f"Hello,{a}")

say_hello("Ganesh")