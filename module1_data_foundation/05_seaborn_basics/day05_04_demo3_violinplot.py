# ==================== violinplot Demo 3：最终高级版（多变量 + 旋转标签 + 业务解读） ====================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

# 只加载你自己的文件
train = pd.read_csv('../data/titanic.csv')

# 主题 + 中文
sns.set_theme(style="darkgrid", palette="husl")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("🚀 violinplot Demo 3 开始（最终高级版）")

# 创建 1×2 子图（同时看年龄和票价）
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Demo 3-左图：年龄分布（按港口）
sns.violinplot(data=train,
               x="Embarked",
               y="Age",
               hue="Survived",
               split=True,
               inner="quart",
               scale="width",
               cut=0,
               palette="husl",
               ax=axes[0])
axes[0].set_title("不同港口乘客年龄分布（生存 vs 死亡）")
axes[0].set_xlabel("登船港口 (S=Southampton, C=Cherbourg, Q=Queenstown)")
axes[0].set_ylabel("年龄")
axes[0].legend(title="是否生存")
axes[0].tick_params(axis='x', rotation=0)

# Demo 3-右图：票价分布（按港口）
sns.violinplot(data=train,
               x="Embarked",
               y="Fare",
               hue="Survived",
               split=True,
               inner="quart",
               scale="width",
               cut=0,
               palette="husl",
               ax=axes[1])
axes[1].set_title("不同港口乘客票价分布（生存 vs 死亡）")
axes[1].set_xlabel("登船港口")
axes[1].set_ylabel("票价 (Fare)")
axes[1].legend(title="是否生存")
axes[1].tick_params(axis='x', rotation=0)

plt.suptitle("Demo 3：泰坦尼克号业务解读 — 港口登船人群特征差异（高级 violinplot）", fontsize=14)
plt.tight_layout()
plt.show()
plt.savefig('violinplot_demo3_advanced_multi.png', dpi=200)

print("✅ Demo 3 完成！")
print("   重点看：")
print("   - 左侧：Cherbourg 上船的人平均年龄更高")
print("   - 右侧：Cherbourg 上船的票价明显更高（富人区）")
print("   - 生存率在不同港口差异巨大")
print("   这张图可以直接放进你的 CSDN 博客作为压轴案例！")