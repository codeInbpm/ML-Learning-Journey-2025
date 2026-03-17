# -*- coding: utf-8 -*-
#==================================== 标准化（StandardScaler）============================================

# 该类是什么特征：
            # 数值特征（连续型数字，如年龄、票价）
# 做什么:
            # 把所有数值转换成均值=0、标准差=1的分布，让不同尺度特征在同一水平线上
# 为什么选这个特征：
            # Age（0-80）和Fare（0-65）尺度完全不同，标准化后模型（线性回归、神经网络、KNN）不会被大数字“欺负”，效果提升明显


import pandas as pd
from sklearn.preprocessing import StandardScaler

# 加载数据
df = pd.read_csv("../../data/titanic.csv")

print("=== 标准化（StandardScaler）Demo ===")

# 1. 选择要处理的数值特征（Age和Fare）
features = ['Age', 'Fare']

# 2. 处理缺失值（先填中位数，避免报错）
df[features] = df[features].fillna(df[features].median())

# 3. 标准化（核心步骤）
scaler = StandardScaler()
df[['Age_std', 'Fare_std']] = scaler.fit_transform(df[features])

# 查看结果
print("标准化前（原始Age和Fare）：")
print(df[features].head())
print("\n标准化后（Age_std和Fare_std）：")
print(df[['Age_std', 'Fare_std']].head())

print("\n标准化后统计：均值≈0，标准差≈1")
print(df[['Age_std', 'Fare_std']].describe().round(4))