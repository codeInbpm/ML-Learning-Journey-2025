import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 主题（Theme）
train = pd.read_csv("../data/titanic.csv")
titanic = sns.load_dataset("titanic")

# === 核心：一键切换主题（试 3 种最常用）===
sns.set_theme(style="darkgrid", palette="husl")     # 推荐！

# sns.set_theme(style="whitegrid", palette="pastel")
# sns.set_theme(style="dark", palette="Set2")
# sns.set_theme(style="ticks", palette="coolwarm")

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

print(titanic.head())

print("✅ 主题设置完成！当前风格：darkgrid + husl")

