# 分组聚合 + 透视表

import pandas as pd
import numpy as np

# 1. 读取原始数据
df = pd.read_csv("../data/titanic.csv")   # 改成你的路径

# 2. 先提取 Title（用于更精准填充年龄）
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)

# 3. 按 Title 分组填充 Age（这是昨天的核心技巧！）
def fill_age_by_title(row):
    if pd.notna(row['Age']):
        return row['Age']
    else:
        # 常见称呼的中位数年龄
        median_ages = {
            'Mr': 30, 'Mrs': 35, 'Miss': 21, 'Master': 4,
            'Dr': 46, 'Rev': 43, 'Col': 58, 'Major': 48, 'Mlle': 24
        }
        return median_ages.get(row['Title'], 30)  # 兜底30岁

df['Age_Filled'] = df.apply(fill_age_by_title, axis=1)

# 4. 现在才可以创建 Age_Group（关键！）
df['Age_Group'] = pd.cut(df['Age_Filled'],
                         bins=[0, 12, 18, 35, 60, 100],
                         labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])

# 5. 新增家庭人数
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1


# 6. 三维透视表：性别 × 舱位 × 年龄段 生还率（神级代码！）
pivot_3d = df.pivot_table(
    values='Survived',
    index=['Sex', 'Pclass'],
    columns='Age_Group',
    aggfunc='mean',
    margins=True  # 自动加总计行/列
).round(3)

print("三维透视表（生还率）：")
print(pivot_3d)

# 7. 家庭人数 vs 生还率 + 人数统计
family_survival = df.groupby('FamilySize')['Survived'].agg(['mean', 'count'])
family_survival.columns = ['生还率', '人数']
family_survival = family_survival.round(3)
print("\n家庭人数影响：")
print(family_survival)

# 8. 票价区间 vs 生还率
fare_bins = pd.cut(df['Fare'], bins=5)
fare_survival = df.groupby(fare_bins)['Survived'].mean().round(3)
print("\n票价区间生还率：")
print(fare_survival)