# ==================== violinplot Basic - Step 1：最简单版本 ====================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')   # 确保窗口弹出

# 只加载你自己的文件
train = pd.read_csv('../data/titanic.csv')

# 主题 + 中文
sns.set_theme(style="darkgrid", palette="husl")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("🚀 violinplot Basic - Step 1 开始（最简单）")

plt.figure(figsize=(8, 5))
sns.violinplot(data=train, x="Survived", y="Age")
plt.title("Basic Step 1：生存 vs 死亡乘客的年龄分布（最简单 violinplot）")
plt.xlabel("是否生存 (0=死亡, 1=生存)")
plt.ylabel("年龄")
plt.show()
plt.savefig('violinplot_basic_step1.png', dpi=200)

print("✅ Basic Step 1 完成！")
print("   重点看：小提琴形状（密度）+ 里面默认带箱线")