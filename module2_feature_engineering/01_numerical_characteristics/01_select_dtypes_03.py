# -*- coding: utf-8 -*-
# =============================异常值处理 + 分箱 =============================

# =============================只针对 Fare（票价） 和 Age（年龄） 两个最典型的数值特征 =============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../../data/titanic.csv")

# ====================== 第三步开始 ======================
print("\n" + "="*50)
print("📋 第三步：异常值处理（Fare） + 分箱（Age & Fare）")
print("="*50)

# 1. 先用箱线图看异常值（视觉化，超级直观）
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 5)) # 创建画布，并设置画布的宽度和高度

plt.subplot(1, 2, 1)    # 创建画布
sns.boxplot(x=df['Age'], color='skyblue')   #箱线图
plt.title('Age 箱线图（异常值很少）') # 文字标题

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Fare'], color='salmon')
plt.title('Fare 箱线图（有很多异常值！）')

plt.tight_layout()  # 防止标签被裁剪，永远在 show() 之前加这一句
plt.show()

# 2. IQR法处理Fare异常值（最常用、最温和的方法）
Q1 = df['Fare'].quantile(0.25)  # 计算第 25 百分位点(第一四分位数)
Q3 = df['Fare'].quantile(0.75)  # 0.75 分位数(第三四分位数)
IQR = Q3 - Q1   # 四分位距
upper_limit = Q3 + 1.5 * IQR    # 上限阈值

print(f"✅ Fare异常值上限：{upper_limit:.2f} 元")
print(f"（超过这个值的票价会被我们“ capping ”）")

# 最安全做法：超过上限的全部设为上限（不删除数据）
df['Fare_capped'] = df['Fare'].clip(upper=upper_limit)

print("\n处理前 Fare 统计：")
print(df['Fare'].describe())

print("\n处理后 Fare_capped 统计：")
print(df['Fare_capped'].describe())


# 3. 分箱（现在绝对不会再有NaN）
from sklearn.preprocessing import KBinsDiscretizer

# 【关键修复】再次确认Age无NaN
df['Age'] = df['Age'].fillna(df['Age'].median())

age_bin = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')
df['Age_bin'] = age_bin.fit_transform(df[['Age']]).astype(int)

fare_bin = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')
df['Fare_bin'] = fare_bin.fit_transform(df[['Fare_capped']]).astype(int)

print("\n分箱后新特征示例（前10行）：")
print(df[['Age', 'Age_bin', 'Fare_capped', 'Fare_bin']].head(10))