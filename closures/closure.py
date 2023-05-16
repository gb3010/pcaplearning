# Outer function
def greeter(name):
    # Inner function
    def greeting():  # Inner function
        return "Hi, " + name

    return greeting  # returning the innter function


val1 = greeter('John')  # Outer function is called. It's scope ends here
print(val1())   # Inner function retains the values even after the outer function's scope is over
val2 = greeter('David')
print(val2())
