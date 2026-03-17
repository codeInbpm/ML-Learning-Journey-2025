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


# Demo 4:广告费 vs 销售额散点图 + 回归线
np.random.seed(10)
ad = np.random.uniform(50,500,100)
sales = ad*2.8 + np.random.normal(0,200,100)

fig, ax = plt.subplots(figsize=(9,7))
ax.scatter(ad, sales, c='#9b59b6', alpha=0.7, s=70, edgecolor='white', linewidth=1)
z = np.polyfit(ad, sales, 1); p = np.poly1d(z)
ax.plot(ad, p(ad), "r--", lw=2, label=f'y={z[0]:.2f}x+{z[1]:.1f}')
ax.set_title('广告投放 vs 销售额相关性', fontsize=16, fontweight='bold')
ax.legend(); ax.grid(alpha=0.3); plt.tight_layout(); plt.show()