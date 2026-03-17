# -*- coding: utf-8 -*-
#==================================== 特征交叉（手动创建新特征）============================================

# 该类是什么特征：
            # 数值特征衍生（交叉组合）
# 做什么:
            # 用Age×Fare、Age/Fare创建新列，捕捉“年龄×财富”这种非线性关系
# 为什么选这个特征：
            # 原始特征往往不够强，交叉后模型效果经常提升10-30%（Kaggle神器）

import pandas as pd

df = pd.read_csv("../../data/titanic.csv")
print("=== 特征交叉Demo ===")

# 先填充缺失值
df['Age'] = df['Age'].fillna(df['Age'].median())

# 创建交叉特征
df['Age_Fare_product'] = df['Age'] * df['Fare']          # 乘法
df['Age_Fare_ratio']   = df['Age'] / (df['Fare'] + 1)    # 除法（+1防除0）
df['Age_bin_Fare']     = df['Age'] // 10 * df['Fare']    # 分箱后交叉

print("新交叉特征示例（前8行）：")
print(df[['Age', 'Fare', 'Age_Fare_product', 'Age_Fare_ratio']].head(8))