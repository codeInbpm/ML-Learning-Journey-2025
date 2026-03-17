# ==================== violinplot Basic - Step 2：加 hue + split ====================

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

print("🚀 violinplot Basic - Step 2 开始（加 hue + split=True）")

plt.figure(figsize=(10, 6))
sns.violinplot(data=train,
               x="Pclass",          # 舱位等级
               y="Age",             # 年龄
               hue="Survived",      # 按生存分组
               split=True,          # ← 最关键！左右分开
               palette="husl")
plt.title("Basic Step 2：不同舱位年龄分布（生存 vs 死亡，split=True）")
plt.xlabel("舱位等级 (1=一等舱, 2=二等舱, 3=三等舱)")
plt.ylabel("年龄")
plt.legend(title="是否生存")
plt.show()
plt.savefig('violinplot_basic_step2_hue_split.png', dpi=200)

print("✅ Basic Step 2 完成！")
print("   重点看：小提琴左右分开（左=死亡，右=生存）")
print("   形状越鼓 = 该年龄段人越多")