import pandas as pd
import numpy as np
import string
from matplotlib import pyplot as plt
import matplotlib

font = {
    'family': 'MicroSoft YaHei',
    'size': 12
}
matplotlib.rc('font', **font)


def test0():
    df = pd.read_csv("./dogNames2.csv")
    # print(df.head())
    # print(df.info())

    # 排序
    df = df.sort_values(by="Count_AnimalName", ascending=False)

    # 取前5行数据
    # print(df.head(5))

    # pandas 取行或列需要注意的点
    # - 方括号写数组，表示取行，对行进行操作
    # - 写字符串，表示取列的索引，对列进行操作

    # 取前20行
    # print(df[:20])

    print("*" * 20)
    # print(df["Row_Labels"])
    # print(type(df["Row_Labels"])) # <class 'pandas.core.series.Series'>
    print(df[:20]["Row_Labels"])


def test1():
    t = pd.DataFrame(np.arange(12).reshape(3, 4),
                     index=list(string.ascii_uppercase[:3]),
                     columns=np.arange(4))

    t.iloc[0, [1, 2]] = None

    t.dropna(axis=0, how='any', inplace=False)

    print(pd.isna(t))


def test2():
    t = pd.read_csv("./IMDB-Movie-Data.csv")

    # Rating 评分
    runtime_data = t["Rating"].values

    plt.figure(figsize=(18, 8), dpi=100)
    plt.hist(runtime_data, 20)

    plt.xlabel('评分')
    plt.ylabel('数量')

    # 生成x
    x = []
    count = 0
    x.append(0)
    while count < 10:
        count += 0.5
        x.append(count)

    plt.xticks(x)

    plt.show()


def test3():
    t = pd.read_csv("./IMDB-Movie-Data.csv")

    # Rating 评分
    runtime_data = t["Rating"].values

    # 平均分
    print('平均分:{}'.format(runtime_data.mean()))

    # 导演人数
    # director_counts = len(set(t['Director'].tolist()))
    director_counts = len(t['Director'].unique())
    print('导演人数:{}'.format(director_counts))

    # 演员人数
    actors_set = set()
    actors0 = t['Actors'].tolist()

    for item in actors0:
        items = item.split(', ')
        for i in items:
            actors_set.add(i)
    print('演员人数:{}'.format(len(actors_set)))

    # 最大最小时长
    time = t['Runtime (Minutes)']
    print('最大时长:{}'.format(time.max()))
    print('最小时长:{}'.format(time.min()))
    print('最小值索引:{}'.format(time.argmin()))
    print('最大值索引:{}'.format(time.argmax()))


def test4():
    t = pd.read_csv("./IMDB-Movie-Data.csv")

    temp_list = t['Genre'].str.split(',').to_list()  # [ ,[],[]]
    # print(temp_list)

    # 提取出所有分类
    genre_set = set()
    for i in temp_list:
        for j in i:
            genre_set.add(j)

    # 构建统计表格
    zeros_df = pd.DataFrame(np.zeros((t.shape[0], len(genre_set))), columns=list(genre_set))
    # print(zeros_df)

    # 每个电影出现分类的位置赋值1
    for i in range(t.shape[0]):
        zeros_df.loc[i, temp_list[i]] = 1

    # 统计每个分类的电影的数量和
    genre_count = zeros_df.sum(axis=0)

    # 排序并绘图
    genre_count = genre_count.sort_values()
    x = genre_count.index
    y = genre_count.values
    plt.figure(figsize=(20, 8), dpi=80)
    plt.bar(range(len(x)), y)
    plt.xticks(range(len(x)), x, rotation=45)
    plt.show()


def test5():
    df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                       ('bird', 'Psittaciformes', 24.0),
                       ('mammal', 'Carnivora', 80.2),
                       ('mammal', 'Primates', np.nan),
                       ('mammal', 'Carnivora', 58)],
                      index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                      columns=('class', 'order', 'max_speed'))

    group0 = df.groupby('class')

    print(group0.head(5))


def test6():
    df = pd.read_csv('./starbucks_store_worldwide.csv')
    df = df[df['Country'] == 'CN']
    group = df.groupby(by=['Country','State/Province'])
    group = group['Brand']

    group_count = group.count()
    print(group_count)
    print(type(group_count))



test6()
