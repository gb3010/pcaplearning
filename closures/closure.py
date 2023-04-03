# Outer function
def greeter(name):
    # Inner function
    def greeting():
        return "Hi, " + name

    return greeting


val1 = greeter('John')
print(val1())
val2 = greeter('David')
print(val2())
