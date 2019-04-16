def test0():
    a = (0, 1, 2, [0, 0])
    a[3].append(666)
    a[3] = 7
    print(a)


test0()
