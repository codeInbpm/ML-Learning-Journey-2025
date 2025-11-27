import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 设置中文字体（防止标题乱码）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']  # Mac/Linux/Windows 都能用
plt.rcParams['axes.unicode_minus'] = False  # 负号正常显示

# ================== 造数据（这一段必须有！）====================
x = np.linspace(0, 10, 200)      # 0~10 之间取 200 个点
y1 = np.sin(x)                   # 正弦
y2 = np.cos(x)                   # 余弦
# ============================================================

# Demo8: 特征相关性热力图
import pandas as pd
np.random.seed(0)
df = pd.DataFrame(np.random.randn(100,6), columns=['年龄','收入','消费','停留时长','点击数','转化'])
corr = df.corr()

fig, ax = plt.subplots(figsize=(8,7))
im = ax.imshow(corr, cmap='RdYlBu_r', vmin=-1, vmax=1)
ax.set_xticks(range(6)); ax.set_yticks(range(6))
ax.set_xticklabels(df.columns); ax.set_yticklabels(df.columns)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

for i in range(6):
    for j in range(6):
        ax.text(j,i,f'{corr.iloc[i,j]:.2f}', ha='center',va='center',
                color='white' if abs(corr.iloc[i,j])>0.6 else 'black', fontweight='bold')

ax.set_title('特征相关性热力图', fontsize=16, fontweight='bold', pad=20)
plt.colorbar(im); plt.tight_layout();
plt.show()