# ==================== Step 2：主题与调色板（修复版） ====================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')          # ← 关键修复！强制弹出窗口（VS Code 最稳）

# 加载数据
train = pd.read_csv('../data/titanic.csv')          # 你的数据
titanic = sns.load_dataset("titanic")               # Seaborn 自带，官方给的测试数据（可以换成自己的文件，如demo03）

# 中文不乱码（必须放最前面）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("✅ 主题设置准备就绪！")

# ====================== 切换主题测试 ======================
# 1. 推荐风格（菜鸟教程 + wangya216 最爱）
sns.set_theme(style="darkgrid", palette="husl")
print("当前风格：darkgrid + husl")

# 测试图1（Seaborn 自带数据）
plt.figure(figsize=(8, 5))
sns.countplot(data=titanic, x="class", hue="survived", palette="husl")
plt.title("泰坦尼克号不同舱位生存情况（darkgrid + husl）")
plt.xlabel("舱位等级")
plt.ylabel("人数")
plt.show()                    # ← 必须有这一行
plt.savefig('seaborn_test1_darkgrid.png', dpi=200)  # 备份：即使不弹出也能看到图片

# 2. 换成另一种风格再跑一次（对比区别）
sns.set_theme(style="whitegrid", palette="pastel")
print("当前风格：whitegrid + pastel")

plt.figure(figsize=(8, 5))
sns.barplot(data=train, x="Pclass", y="Survived", hue="Sex", palette="pastel")
plt.title("不同舱位生存率（whitegrid + pastel）")
plt.show()
plt.savefig('seaborn_test2_whitegrid.png', dpi=200)

# 3. 再试一种（黑暗风）
sns.set_theme(style="dark", palette="Set2")
print("当前风格：dark + Set2")

plt.figure(figsize=(8, 5))
sns.boxplot(data=train, x="Pclass", y="Age", hue="Survived", palette="Set2")
plt.title("不同舱位年龄分布（dark + Set2）")
plt.show()
plt.savefig('seaborn_test3_dark.png', dpi=200)

print("🎉 三张图已生成！请检查：")
print("   1. 窗口是否弹出？")
print("   2. 文件夹里是否多了 3 张 PNG？")