from matplotlib import pyplot as plt


def test0():
    # 设置图片的大小
    fig = plt.figure(figsize=(10, 5), dpi=100)

    x = range(2, 26, 2)
    y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

    plt.xticks(range(2, 26))
    plt.yticks(range(min(y), max(y) + 1))

    plt.plot(x, y)
    plt.show()


test0()
