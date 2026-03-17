# ==================== violinplot Basic - Step 3：最终进阶版（inner + scale + cut） ====================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')   # 确保窗口弹出

# 只加载你自己的文件
train = pd.read_csv('../../data/titanic.csv')

# 主题 + 中文
sns.set_theme(style="darkgrid", palette="husl")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("🚀 violinplot Basic - Step 3 开始（最终进阶版）")

plt.figure(figsize=(10, 6))
sns.violinplot(data=train,
               x="Pclass",
               y="Age",
               hue="Survived",
               split=True,
               inner="quart",           # 显示四分位数线
               scale="count",           # 宽度按人数自动调整
               cut=0,                   # 不超出实际数据范围
               palette="husl")
plt.title("Basic Step 3：不同舱位年龄分布（最终进阶版）")
plt.xlabel("舱位等级 (1=一等舱, 2=二等舱, 3=三等舱)")
plt.ylabel("年龄")
plt.legend(title="是否生存")
plt.xticks(rotation=0)               # 标签不旋转
plt.show()
plt.savefig('violinplot_basic_step3_advanced.png', dpi=200)

print("✅ Basic Step 3 完成！")
print("   重点看：")
print("   1. 小提琴里面出现了四分位数横线（inner='quart'）")
print("   2. 宽度不一样（人数越多越宽）")
print("   3. 小提琴边缘整齐（cut=0）")