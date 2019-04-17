import os


def test0():
    abs_path = os.path.abspath('test.txt')
    print(abs_path)


if __name__ == '__main__':
    test0()
