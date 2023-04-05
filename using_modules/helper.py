# Defining functions to be called in from the module
def extract_upper(name):
    return list(filter(str.isupper, name))


def extract_lower(name):
    return list(filter(str.islower, name))
