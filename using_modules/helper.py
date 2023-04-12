# Defining functions to be called in from the module

# Making only extract_upper callable while importing all
#__all__ = ['extract_upper']


def extract_upper(name):
    return list(filter(str.isupper, name))


# Making extract_lower a private function which is not imported by default
def _extract_lower(name):
    return list(filter(str.islower, name))


if __name__ == "__main__":
    print("Hello from Helper")
