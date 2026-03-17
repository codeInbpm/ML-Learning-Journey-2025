# ==================== violinplot Demo 1：票价分布（最实用业务案例） ====================

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

print("🚀 violinplot Demo 1 开始（票价分布）")

plt.figure(figsize=(10, 6))
sns.violinplot(data=train,
               x="Pclass",
               y="Fare",
               hue="Survived",
               split=True,
               inner="quart",
               scale="count",
               cut=0,
               palette="husl")
plt.title("Demo 1：不同舱位票价分布（生存 vs 死亡）")
plt.xlabel("舱位等级 (1=一等舱, 2=二等舱, 3=三等舱)")
plt.ylabel("票价 (Fare)")
plt.legend(title="是否生存")
plt.show()
plt.savefig('violinplot_demo1_fare.png', dpi=200)

print("✅ Demo 1 完成！")
print("   重点看：")
print("   - 一等舱票价分布最宽（有超级贵的票）")
print("   - 三等舱票价很集中且便宜")
print("   - 生存者（右边）票价普遍更高")