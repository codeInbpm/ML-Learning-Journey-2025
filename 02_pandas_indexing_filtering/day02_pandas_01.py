# 布尔索引高级玩法

import pandas as pd
df = pd.read_csv("../data/titanic.csv")

# 1. 同时满足3个条件：女性 + 头等舱 + 年龄<30
female_first_young = df[(df['Sex'] == 'female') &
                        (df['Pclass'] == 1) &
                        (df['Age'] < 30)]
print("匹配乘客数量：", len(female_first_young))
print(female_first_young[['Name', 'Age', 'Pclass', 'Survived']].head(3))


# 2. 任意一个条件：儿童（<12）或老人（>60）
children_or_senior = df[(df['Age'] < 12) | (df['Age'] > 60)]
print("\n儿童或老人数量：", len(children_or_senior))
print("他们的生还率：", children_or_senior['Survived'].mean())

# 3. .query() 一行搞定复杂筛选
query_result = df.query("Sex == 'female' and Pclass == 1 and Age < 30")
print("\nQuery结果数量：", len(query_result))

# 4. 反向筛选：非条件（~ 取反）
not_first_class = df[~ (df['Pclass'] == 1)]
print("\n非头等舱乘客：", len(not_first_class))