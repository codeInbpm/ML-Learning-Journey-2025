import pandas as pd
df = pd.read_csv("../data/titanic.csv")

print("1. 查看数据的前10行")
print(df.head(10))

print("查看数据的最后 10 行")
print(df.tail(10))

print("查看数据的前 10 行和后 7 行")
print(pd.concat([df.head(10), df.tail(7)], axis=0))

print("筛选所有女性乘客")
female = df[df['Sex'] == 'female']
print(female)

print("筛选头等舱且年龄 > 30 的乘客")
rich_old = df[(df['Pclass'] == 1) & (df['Age'] > 30)]
print(rich_old[['Name', 'Age', 'Fare']].head())

print("生还率最高的性别是？")
surival_high_sex = df.groupby('Sex')['Survived'].mean()
print(surival_high_sex)

print("新增 FamilySize 列（兄弟姐妹 + 父母子女 + 自己）")
df['FamilySize'] = df['SibSp'] + df['Parch']
print(df[['Name', 'FamilySize', 'SibSp', 'Parch']].head())


print("用 apply 自定义函数：票价等级")
def fare_level(fare):
    if fare <= 10 :return 'Cheap'
    elif fare <= 30: return 'Medium'
    elif fare <= 40: return 'Hard'
    else:return 'Expensive'

df['Fare_Level'] = df['Fare'].apply(fare_level)
print(df['Fare_Level'].value_counts())

print("找出最贵的10张票是谁买的？")
print(df.nlargest(10, 'Fare')[['Name', 'Fare', 'Pclass', 'Cabin']])
