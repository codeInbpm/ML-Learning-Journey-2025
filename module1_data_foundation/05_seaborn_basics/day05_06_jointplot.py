import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

train = pd.read_csv('../data/titanic.csv')
sns.set_theme(style="whitegrid")

print("🚀 Jointplot 学习开始：探索年龄与票价的关系")

# 绘制回归联合图
# 它会在中间画散点和回归线，顶部和右侧画直方图
g = sns.jointplot(data=train, x="Age", y="Fare", kind="reg", color="m", height=7)

plt.suptitle("年龄与票价的联合分布 (带回归线)", y=1.02)
plt.show()