# ==================== Sub-Step 3.2：barplot 多个 Demo（只用你的 train.csv） ====================
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

train = pd.read_csv('../../data/titanic.csv')

sns.set_theme(style="darkgrid", palette="husl")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("🚀 开始 barplot 学习 - 4 个 Demo")

# Demo 1：最基础（平均生存率）
plt.figure(figsize=(8, 5))
sns.barplot(data=train, x="Pclass", y="Survived")
plt.title("Demo 1：不同舱位平均生存率")
plt.xlabel("舱位等级")
plt.ylabel("生存率")
plt.show()
plt.savefig('barplot_demo1_basic.png', dpi=200)

# Demo 2：加 hue + 误差棒（最常用！）
plt.figure(figsize=(8, 5))
sns.barplot(data=train, x="Pclass", y="Survived", hue="Sex", palette="husl")
plt.title("Demo 2：不同舱位生存率（按性别分组）")
plt.legend(title="性别")
plt.show()
plt.savefig('barplot_demo2_hue.png', dpi=200)

# Demo 3：换 y 轴为数值（平均票价）
plt.figure(figsize=(8, 5))
sns.barplot(data=train, x="Pclass", y="Fare", hue="Survived", palette="Set2")
plt.title("Demo 3：不同舱位平均票价（生存 vs 死亡）")
plt.show()
plt.savefig('barplot_demo3_fare.png', dpi=200)

# Demo 4：横向 + 排序
plt.figure(figsize=(8, 6))
sns.barplot(data=train, y="Embarked", x="Age", hue="Survived",
            palette="coolwarm", orient="h", order=["S", "C", "Q"])
plt.title("Demo 4：不同港口平均年龄（横向）")
plt.show()
plt.savefig('barplot_demo4_horizontal.png', dpi=200)

print("✅ barplot 4 个 Demo 完成！")