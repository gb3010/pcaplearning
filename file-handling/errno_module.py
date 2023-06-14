#!/usr/loca/bin/python3
import errno

try:
    with open("no_such_file.txt") as f:
        z = f.read()
except OSError as e:
    # print(e.errno, e.strerror)
    if e.errno == errno.ENOENT:
        print("No such file or directory")
    elif e.errno == errno.EACCES:
        print("Bad permissions")

