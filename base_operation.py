# -*- coding: utf-8 -*-
'''
基本操作
'''
import numpy as np
import pandas as pd
from pylab import *

# 随机数据
dates = pd.date_range("20170301", periods=8)


def base_data():
    # 基本数据结构 Data Structure
    s = pd.Series([i * 2 for i in range(1, 11)])
    # 随机数据
    dates = pd.date_range("20170301", periods=8)
    # DataFrame 数据结构
    ## 定义方式一
    ###  index表示主键  columns属性值
    df = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list("ABCDE"))
    return df


def test1(df):
    '''
    base基本操作
    '''

    ## 打印前几行
    print(df.head(3))

    ## 打印后几行
    print(df.tail(3))

    ## 打印主键
    print(df.index)

    ## 打印值
    print(df.values)

    ## 横纵列转换格式
    print(df.T)

    ## 查看 根据某一列排序 降序
    print(df.sort_values("C"))

    ## 根据index 进行排序  并且禁止降序处理
    print(df.sort_index(axis=1, ascending=False))

    ## 大致了解数据   求出所有属性值的 最大值 最小值 平均值
    print(df.describe())

    print("=" * 100)


def test2(df):
    '''
    选择数据  切片
    '''
    # 直接打印A的属性列
    print(df["A"])

    # 获取0-3行的数据 切片
    print(df[:3])

    # 获取1号-4号的数据 切片
    print(df["20170301":"20170304"])

    # 提取指定主键的数据
    print(df.loc[dates[0]])
    # 获取指定范围数据 并且提取指定属性
    print(df.loc["20170301":"20170304", ["B", "D"]])

    # 根据主键  ->获取指定的属性
    print(df.at[dates[0], "C"])

    # 根据下标 获取指定行数数据
    print(df.iloc[1:3, 2:4])
    # 根据下标 获取第0行第四列的值
    print(df.iloc[0, 4])
    # 跟上面类似 获取指定位置的值
    print(df.iat[0, 4])

    '''
    筛选数据
    '''
    ## 筛选符合 B>0 和A<0的记录
    print(df[df.B > 0][df.A < 0])
    ## 筛选 df内所有值>0的 不符合为NaN
    print(df[df > 0])

    ## 筛选 E属性存在某个几个值的 类似 数据库的in
    print(df[df["E"].isin([1, 2])])


def test3(df):
    '''
    dataFrame赋值
    '''
    # 创建一个新的数据项
    s1 = pd.Series(list(range(10, 18)), index=pd.date_range("20170301", periods=8))
    ## 赋值  根据主键将数据赋值给F
    df["F"] = s1

    ## at 根据指定位置赋值
    df.at[dates[0], "A"] = 0

    ## iat  在数据网格的1,1的位置   进行修改赋值
    df.iat[1, 1] = 1
    ## loc 选择属性 替换所有 直接赋值
    df.loc[:, "D"] = 1


def test4(df):
    '''
    拷贝一份dataFrame
    '''
    df2 = df.copy()
    ## 所有正数修改为负数
    df2[df2 > 0] = -df2
    print(df2)


def test5(df):
    '''
    缺失值处理
    '''
    ## 获取原数据的前4行 获取属性 ABCD 新增G属性
    df1 = df.reindex(index=dates[:4], columns=list("ABCD") + ["G"])
    ## 仅给第一行第二行 赋值
    df1.loc[dates[0]:dates[1], "G"] = 1
    # print(df1)

    # 列表返回true false
    print(pd.isnull(df1))

    # 列表返回false true
    print(pd.notnull(df1))

    # 删除列
    del df1['A']
    # 查询列名
    print(df1.columns)

    # 对于dataFrame 可以删除任意轴上的索引值
    print(df1.drop([dates[0], dates[2]]))

    ## 缺失值处理方式
    ### 一  ->直接丢弃
    print(df1.dropna())
    ### 二 ->赋值一个指定值 或者插值
    print(df1.fillna(value=2))


def test6(df):
    '''
    科学计算
    '''
    # 求平均值
    print(df.mean())
    # 方差
    print(df.var())

    s = pd.Series([1, 2, 4, np.nan, 5, 7, 9, 10], index=dates)
    print(s)
    # 所有的值移后两位 后面的值不会移动至前面
    print(s.shift(2))

    # 阶分 填入数值表示多阶 后面一个减去前面一个
    print(s.diff())

    # 每个值在series出现的次数
    print(s.value_counts())

    print(df)
    # 累加 后面的值都是前面的累加值
    print(df.apply(np.cumsum))

    # 自定义  极差
    print(df.apply(lambda x: x.max() - x.min()))


def test7(df):
    '''
    拼接
    '''
    # 获取前三行后三行
    pieces = [df[:3], df[-3:]]
    # 拼接
    print(pd.concat(pieces))

    left = pd.DataFrame({"key": ["x", "y"], "value": [1, 2]})
    right = pd.DataFrame({"key": ["x", "z"], "value": [3, 4]})

    #   合并  类似数据库的left join   对比两个DataFrame  on=对比的key how=默认inner  left right outer(全部显示)
    print(pd.merge(left, right, on="key", how="left"))

    df3 = pd.DataFrame({"A": ["a", "b", "c", "b"], "B": list(range(4))})

    # 聚合函数 类似数据库的group by
    print(df3.groupby("A").sum())


def test8(df):
    '''
    重塑 透视表->交叉分析
    '''
    import datetime
    df4 = pd.DataFrame({"A": ['one', 'one', 'two', 'three'] * 6,
                        "B": ['a', 'b', 'c'] * 8,
                        "C": ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                        "D": np.random.randn(24),
                        # 状态分布
                        "E": np.random.randn(24),
                        "F": [datetime.datetime(2017, i, 1) for i in range(1, 13)] +
                             [datetime.datetime(2017, i, 15) for i in range(1, 13)]})

    # 透视表
    ## 输出值:D 主键:AB 字段:C
    print(pd.pivot_table(df4, values="D", index=["A", "B"], columns=["C"]))


def test9(df):
    '''
    时间序列
    time series
    '''
    # 定义时间序列 periods=时间段 feq:时间格式 Y M H D S
    t_exam = pd.date_range("20170301", periods=10, freq="S")
    print(t_exam)

    '''
    位图功能 
    Graph
    '''
    # 创建序列
    ts = pd.Series(np.random.randn(1000), index=pd.date_range("20170301", periods=1000))
    # 累加
    ts = ts.cumsum()
    # 需要引入  from pylab import *
    ts.plot()
    show()


def test10(df):
    '''
    文件操作
    '''
    # 读取csv文件
    df6 = pd.read_csv("./test.csv")
    print(df6)
    # 读取xlsx文件 第一块
    df7 = pd.read_excel("./test.xlsx", "Sheet1")
    print(df7)

    # 保存csv
    df6.to_csv("/test2.csv")
    # 保存xlsx
    df7.to_excel("/test2.xlsx")


if __name__ == '__main__':
    df = base_data()
    # test1(df)
    # test2(df)
    # test3(df)
    # test4(df)
    # test5(df)
    # test6(df)
    # test7(df)
    # test8(df)
    # test9(df)
    test10(df)
