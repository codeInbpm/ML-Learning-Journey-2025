# -*- coding: utf-8 -*-
#==================================== 缺失值填充（SimpleImputer） ============================================

# 该类是什么特征：
            # 数值特征（有NaN）
# 做什么:
            # 用中位数/均值/常数把NaN填满（Age有177个缺失）
# 为什么选这个特征：
            # 模型无法处理NaN，必须先填；中位数最稳健（不受极端值影响）
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv("../../data/titanic.csv")
print("=== 缺失值填充Demo ===")

print("填充前Age缺失值数量：", df['Age'].isnull().sum())

# 中位数填充（最推荐）
imputer = SimpleImputer(strategy='median')
df['Age_filled'] = imputer.fit_transform(df[['Age']])

print("填充后缺失值数量：", df['Age_filled'].isnull().sum())
print("填充后Age统计：")
print(df['Age_filled'].describe().round(2))