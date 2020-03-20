import sys
import string


def test0():
    print(sys.path)


def test1():
    a = [i * 2 for i in range(0, 11)]
    print(a)


def test2():
    a = {string.ascii_uppercase[i]: i for i in range(10)}
    print(a)
    print(type(a))


test2()
