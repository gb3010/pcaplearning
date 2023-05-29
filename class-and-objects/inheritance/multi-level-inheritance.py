#!/usr/local/bin/python3

class GrandParent:
    def gp_unique_detail(self):
        print("Has blue eyes")


class Parent(GrandParent):
    def parent_unique_detail(self):
        print("Has sharp nose")


class GrandChild(Parent):
    pass

# Syntax to check if a class is a subclass of another
# >>> issubclass(GrandChild,Parent)
# True
# >>> issubclass(GrandChild,GrandParent)
# True
# >>> issubclass(GrandParent,Parent)
# False

# Syntax to check the base / parent classes of child class
# >>> GrandChild.__bases__
# (<class '__main__.Parent'>,)
# >>> GrandChild.__bases__
# (<class '__main__.Parent'>,)
# >>> Parent.__bases__
# (<class '__main__.GrandParent'>,)


# Syntax to print child classes of a base class
# >>> GrandParent.__subclasses__()
# [<class '__main__.Parent'>]
