x = [1, 5, 2, 11, 9, 22, 33, 14, 3]
# Function to sort in ascending order
y = sorted(x)
print(y)

# Function to sort in descending order
reverse_list = sorted(x, reverse=True)
print(reverse_list)


# Function to sort a list based on a key
# A Key can be anything such as length of the list element
# Or, even a function

# Function to define a key
def func(n):
    return n % 3


mod_3_list = sorted(x, key=func)
print(mod_3_list)
