# ==================== violinplot Demo 2：violinplot + swarmplot 叠加真实点 ====================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

# 只加载你自己的文件
train = pd.read_csv('../../data/titanic.csv')

# 主题 + 中文
sns.set_theme(style="darkgrid", palette="husl")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("🚀 violinplot Demo 2 开始（violin + swarm 叠加真实数据点）")

plt.figure(figsize=(11, 7))

# 1. 先画 violinplot（把 inner 关掉，避免和点重叠）
sns.violinplot(data=train,
               x="Pclass",
               y="Age",
               hue="Survived",
               split=True,
               inner=None,          # 关掉内部箱线，让 swarm 更清晰
               scale="count",
               cut=0,
               palette="husl")

# 2. 再叠加 swarmplot（真实数据点）
sns.swarmplot(data=train,
              x="Pclass",
              y="Age",
              hue="Survived",
              dodge=True,          # 左右分开不重叠
              palette="husl",
              size=3,              # 点的大小
              alpha=0.7)           # 半透明

plt.title("Demo 2：不同舱位年龄分布（violinplot + swarmplot 叠加真实点）")
plt.xlabel("舱位等级 (1=一等舱, 2=二等舱, 3=三等舱)")
plt.ylabel("年龄")
plt.legend(title="是否生存")
plt.show()
plt.savefig('violinplot_demo2_violin_swarm.png', dpi=200)

print("✅ Demo 2 完成！")
print("   重点看：")
print("   - 小提琴显示密度分布")
print("   - 每个黑点都是一个真实乘客（不重叠）")
print("   - 生存者（右边）在高龄段更密集")