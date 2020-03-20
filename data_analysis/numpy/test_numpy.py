import numpy as np


def test0():
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = np.array(range(1, 10))
    c = np.arange(1, 10)

    print(a.dtype)


def test1():
    file = './GB_video_data_numbers.csv'

    t1 = np.loadtxt(file, dtype='int', delimiter=',', unpack=False)

    print(t1)


def test2():
    t = np.arange(12)
    print(t)

    # 将t转换为3行4列的矩阵
    t1 = t.reshape(3, 4)
    print('*' * 10)
    print(t1)

    t2 = t1.astype("float")
    print('*' * 10)
    print(t2)

    t2[1, 2:] = np.nan
    print('*' * 10)
    print(t2)

    for i in range(t1.shape[1]):
        temp_col = t2[:, i]  # 选取当前一列
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:
            temp_not_man_col = temp_col[temp_col == temp_col]
            temp_col[np.isnan(temp_col)] = temp_not_man_col.mean()

    print('*' * 10)

    print(t2)


def test3():
    file = './GB_video_data_numbers.csv'

    t1 = np.loadtxt(file, dtype='int', delimiter=',', unpack=False)

    print(t1)

    t1_commonts = t1[:,3]
    print('*'*20)
    print(t1_commonts)

    t1_commonts_min = t1_commonts.min()
    t1_commonts_max = t1_commonts.max()
    print('{}--{}'.format(t1_commonts_min,t1_commonts_max))


test3()
