# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


'''
基础数据结构
'''
def test():
    # 基本数据结构 Data Structure
    s = pd.Series([i * 2 for i in range(1, 11)])
    print(type(s))
    # 随机数据
    dates = pd.date_range("20170301", periods=8)

    # DataFrame 数据结构
    ## 定义方式一
    ###  index表示主键  columns属性值
    df = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list("ABCDE"))
    print(df)
    ## 定义方式二
    df1 = pd.DataFrame({"A": 1,
                        "B": pd.Timestamp("20170301"),
                        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                        "D": np.array([3] * 4, dtype="float32"),
                        "E": pd.Categorical(["police", "student", "teacher", "doctor"])})
    print(df1)

    pass


if __name__ == '__main__':
    test()
