def test0():
    print("gg" in "eggs")
    print('-----------------------------1---------------------------------')
    print('\n')

    lists = [[]] * 3
    print(lists)

    lists[0].append(3)
    lists[1].append(31)
    print(lists)
    print('-----------------------------2---------------------------------')
    print('\n')

    lists = [[] for i in range(3)]
    lists[0].append(3)
    lists[1].append(5)
    lists[2].append(7)
    print(lists)
    print('-----------------------------2---------------------------------')
    print('\n')

    lists = [1, 2, 3, 4]
    lists.extend([33, 44, 9])
    lists.sort()
    print(lists)
    l1 = lists.index(44)
    print(l1)

    l2 = [1, 55, 4, 4, 7, 8]
    del l2[0]
    print(l2)
    del l2[1:2]
    print(l2)
    l2.pop()
    print(l2)
    l2[0:2] = []
    print(l2)
    l2[1:4] = [11, 22, 33]
    print(l2)
    print('-----------------------------3---------------------------------')
    print('\n')

    r = range(10)
    print(r)
    t1 = tuple(r)
    print(t1)
    t2 = t1[1:]
    print(t2)
    print('-----------------------------4---------------------------------')
    print('\n')


def test1():
    a = [1, 2]
    b = [3, 4]
    print(a + b)
    print(a * 5)


def test2():
    a = [1, 2, 3, 4, [666, 777]]
    b = a[:]
    b[4] = [888, 999]

    print(a)
    print(b)


test2()
