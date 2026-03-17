# =============================看缺失值 → 填充Age缺失 → 画直方图看分布 =============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../../data/titanic.csv")

# ====================== 第二步开始 ======================
print("\n" + "="*50)
print("📋 第二步：查看缺失值 + 处理Age缺失 + 画分布图")
print("="*50)

# 1. 查看完整信息（重点看 Non-Null Count）
print(df.info())

# 2. 处理缺失值：Age列用中位数填充（最常用、最安全的方法）
print("\nAge缺失值数量（填充前）：", df['Age'].isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].median())   # ← 核心一行代码
print("Age缺失值数量（填充后）：", df['Age'].isnull().sum())

# 3. 填充后再次看统计（确认Age现在是891条）
print("\n填充后Age的统计：")
print(df['Age'].describe())

# 4. 画直方图（看分布形状）
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 5))

# Age分布
plt.subplot(1, 2, 1)
sns.histplot(df['Age'], kde=True, bins=30, color='skyblue')
plt.title('Age 分布图（填充后）')
plt.xlabel('年龄')

# Fare分布（票价，后面要重点处理）
plt.subplot(1, 2, 2)
sns.histplot(df['Fare'], kde=True, bins=30, color='salmon') # 绘制直方图（Histogram）并叠加核密度估计曲线（KDE）
plt.title('Fare 票价分布图')
plt.xlabel('票价')

plt.tight_layout()
plt.show()   # ← 这行会弹出图片窗口