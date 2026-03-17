# -*- coding: utf-8 -*-
#==================================== 归一化（MinMaxScaler） ============================================

# 该类是什么特征：
            # 数值特征（连续型数字）
# 做什么:
            # 把数值压缩到0~1之间（最小值→0，最大值→1）
# 为什么选这个特征：
            # 神经网络、决策树、距离类算法（如KNN）对0-1范围更敏感，避免某个特征“一家独大”

import pandas as pd
# MinMaxScaler：  归一化器。将所有数值压缩到 $[0, 1]$ 之间。
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("../../data/titanic.csv")
print("=== 归一化（MinMaxScaler）Demo ===")

features = ['Age', 'Fare']
df[features] = df[features].fillna(df[features].median())  # 补全缺失值

# 归一化（核心）
scaler = MinMaxScaler()
# fit : 学习阶段。计算数据的最大值（Max）和最小值（Min）。
# transform: 执行阶段。根据算好的 Max/Min 进行数学转换。
# fit_transform	 组合拳。一次性完成学习和转换。
df[['Age_mm', 'Fare_mm']] = scaler.fit_transform(df[features])

print("归一化后（0~1范围）：")
print(df[['Age_mm', 'Fare_mm']].head())
print("\n最小值和最大值：")
print(df[['Age_mm', 'Fare_mm']].describe().loc[['min', 'max']].round(4))