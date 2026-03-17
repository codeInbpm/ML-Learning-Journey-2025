# -*- coding: utf-8 -*-
#==================================== 异常值处理（IQR Capping） ============================================

# 该类是什么特征：
            # 数值特征（有极端值）
# 做什么:
            # 把Fare里512元这种超级异常值“压”到合理上限（不删除数据）
# 为什么选这个特征：
            # 极端值会把模型拉歪（尤其是线性模型），capping是最温和有效的处理方式
# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("../../data/titanic.csv")
print("=== 异常值处理（IQR Capping）Demo ===")

# 计算IQR
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + 1.5 * IQR

print(f"Fare异常值上限：{upper_limit:.2f}")

# capping（超过上限的全部设为上限）
df['Fare_capped'] = df['Fare'].clip(upper=upper_limit)

print("\n处理前最大值：", df['Fare'].max())
print("处理后最大值：", df['Fare_capped'].max())
print(df[['Fare', 'Fare_capped']].describe().round(2))