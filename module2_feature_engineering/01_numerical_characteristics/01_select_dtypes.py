# =============================加载数据 + 认识数值特征 ============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../../data/titanic.csv")

print("✅ 数据加载成功！前5行长这样：")
print(df.head())

print("\n📊 数据整体信息（看哪列是数值）：")
print(df.info())

print("\n🔢 数值特征的统计（重点看！）：")
pd.set_option('display.max_columns', None)  # 如果打印结果有部分数据被隐藏
# 计算数据里所有数值型列的统计摘要
print(df.describe())

print("\n📌 当前所有的数值特征列：")
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(numerical_cols)