# -*- coding: utf-8 -*-
#==================================== 离散化（分箱 / KBinsDiscretizer） ============================================

# 该类是什么特征：
            # 数值特征（连续型 → 类别型）
# 做什么:
            # 把连续数字切成固定几个“箱子”（如0-4），把Age变成“青年/中年/老年”标签
# 为什么选这个特征：
            # 模型更容易学习非线性关系，减少极端值影响，防止过拟合（Kaggle上常用）
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

df = pd.read_csv("../../data/titanic.csv")
print("=== 离散化（分箱）Demo ===")

features = ['Age', 'Fare']
df[features] = df[features].fillna(df[features].median())

# 分箱（等频分箱，5个箱子）
binner = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')
                        # n_bins=5	箱子数量
                        # strategy='quantile'	切分策略：等频（没个箱子里数量几乎一样多）
                        # strategy='uniform'	切分策略：等距     按照数值范围平分（比如 0-100 岁，每 20 岁一组）。

# Fit（计算边界）根据算出的边界，

# Transform（映射标签）：
        # 将每个人的原始年龄映射到对应的 ID 上。     22 岁 落在 [19, 25] 区间内，所以赋值为 1。
df[['Age_bin', 'Fare_bin']] = binner.fit_transform(df[features]).astype(int)

print("分箱后（0~4类别）：")
print(df[['Age', 'Age_bin', 'Fare', 'Fare_bin']].head(10))