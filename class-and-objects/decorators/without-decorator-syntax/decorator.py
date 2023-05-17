def decorator(func):
    def inner():
        print("This is added from the decorator")
        func()

    return inner

def greet():
    print("Hello World!")


greet = decorator(greet)
greet()