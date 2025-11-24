# 缺失值填充策略

import pandas as pd
df = pd.read_csv("../data/titanic.csv")

# 1. 先提取Title
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
print("称呼分布：")
print(df['Title'].value_counts().head())

# 2. Age: 按Title分组填中位数（Mr用Mr的中位数，更精准！）
title_age_median = df.groupby('Title')['Age'].median()
def fill_age(row):
    return row['Age'] if pd.notna(row['Age']) else title_age_median[row['Title']]
df['Age_Filled'] = df.apply(fill_age, axis=1)
print("\nAge填充前后缺失：", df['Age'].isnull().sum(), "→", df['Age_Filled'].isnull().sum())

# 3. Embarked: 众数填充（最常见值）
embarked_mode = df['Embarked'].mode()[0]
df['Embarked_Filled'] = df['Embarked'].fillna(embarked_mode)
print("Embarked填充：2 → 0")

# 4. Cabin: 提取甲板字母（C/A/B等），缺失标'M'
df['Cabin_Deck'] = df['Cabin'].str[0].fillna('M')
print("\n甲板分布：")
print(df['Cabin_Deck'].value_counts())
