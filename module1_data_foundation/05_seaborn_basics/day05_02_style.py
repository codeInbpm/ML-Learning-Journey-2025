import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. 加载数据 (使用你本地的文件)
train = pd.read_csv("../../data/titanic.csv")

# 2. 设置主题
sns.set_theme(style="darkgrid", palette="husl")

# 3. 中文支持设置
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 4. 打印数据确认
print(train.head())

# 5. 【关键】添加绘图代码
plt.figure(figsize=(8, 5))
sns.barplot(data=train, x="Sex", y="Survived") # 画一个性别与生存率的柱状图
plt.title("不同性别的生存率测试 (Style: darkgrid)")

# 6. 【关键】弹出图表
plt.show()

print("✅ 图表应已弹出！")