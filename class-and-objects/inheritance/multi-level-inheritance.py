#!/usr/local/bin/python3

class GrandParent:
    def gp_unique_detail(self):
        print("Has blue eyes")


class Parent(GrandParent):
    def parent_unique_detail(self):
        print("Has sharp nose")


class GrandChild(Parent):
    pass

