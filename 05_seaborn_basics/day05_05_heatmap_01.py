#           相关性矩阵
# ==================== heatmap Basic - Step 1：相关性热力图 ====================
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

# 1. 加载数据
train = pd.read_csv('../data/titanic.csv')

# 2. 准备数据：heatmap 需要数值型数据
# 我们选取几个关键的数值列计算相关性系数 (.corr())
# 相关系数范围 [-1, 1]，1表示正相关，-1表示负相关
numeric_train = train.select_dtypes(include=['float64', 'int64'])
corr_matrix = numeric_train.corr()

# 3. 设置主题
sns.set_theme(style="white")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("🚀 Heatmap Step 1 开始：相关性分析")

plt.figure(figsize=(10, 8))
# 绘制热力图
sns.heatmap(data=corr_matrix,
            annot=True,       # 显示数值
            fmt=".2f",        # 保留两位小数
            cmap="coolwarm",  # 冷暖色调（适合看正负相关）
            linewidths=0.5)

plt.title("Titanic 数据集特征相关性热力图")
plt.show()
plt.savefig('heatmap_step1_corr.png', dpi=200)

print("✅ Heatmap Step 1 完成！")
print("   重点看：对角线为什么全是 1.0？哪些特征之间颜色最深？")