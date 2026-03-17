# ==================== Sub-Step 3.1：countplot 多个 Demo（只用你的 train.csv） ====================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')   # 确保窗口弹出

# ==================== 只加载你自己的文件 ====================
train = pd.read_csv('../../data/titanic.csv')

# 统一主题 + 中文（保持你喜欢的风格）
sns.set_theme(style="darkgrid", palette="husl")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("🚀 开始 countplot 学习 ")

# 先看一眼数据结构（帮你彻底明白“舱位等级”从哪里来）
print("你的 train.csv 列名：", train.columns.tolist())
print("\nPclass 各舱位人数统计：\n", train['Pclass'].value_counts())

# ==================== Demo 1：最基础（只用你的数据） ====================
plt.figure(figsize=(8, 5))
sns.countplot(data=train, x="Pclass")
plt.title("Demo 1：不同舱位乘客人数（最简单 countplot）")
plt.xlabel("舱位等级 (1=一等舱, 2=二等舱, 3=三等舱)")
plt.ylabel("人数")
plt.show()
plt.savefig('countplot_demo1_basic.png', dpi=200)

# ==================== Demo 2：加 hue 分组（最常用！） ====================
plt.figure(figsize=(8, 5))
sns.countplot(data=train, x="Pclass", hue="Survived", palette="husl")
plt.title("Demo 2：不同舱位生存 vs 死亡人数（加 hue 分组）")
plt.xlabel("舱位等级")
plt.ylabel("人数")
plt.legend(title="是否生存 (0=死亡, 1=生存)")
plt.show()
plt.savefig('countplot_demo2_hue.png', dpi=200)

# ==================== Demo 3：排序 + 自定义颜色 ====================
plt.figure(figsize=(10, 6))
sns.countplot(data=train, x="Embarked", hue="Pclass",
              palette="Set2",
              order=["S", "C", "Q"])   # 手动排序
plt.title("Demo 3：不同港口登船人数（按舱位分组 + 排序）")
plt.xlabel("登船港口 (S=Southampton, C=Cherbourg, Q=Queenstown)")
plt.ylabel("人数")
plt.show()
plt.savefig('countplot_demo3_order.png', dpi=200)

# ==================== Demo 4：横向图 ====================
plt.figure(figsize=(8, 6))
sns.countplot(data=train, y="Sex", hue="Survived", palette="coolwarm", orient="h")
plt.title("Demo 4：男女生存人数（横向柱状图）")
plt.ylabel("性别")
plt.xlabel("人数")
plt.legend(title="是否生存")
plt.show()
plt.savefig('countplot_demo4_horizontal.png', dpi=200)

print("✅ 4 个 countplot Demo 全部完成！")
print("   只用了你的 train.csv，所有图都和前4天数据一致")
print("   文件夹里多了 4 张 PNG，可直接放博客")