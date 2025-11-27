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


# Demo 3：用户年龄分布直方图 + 正态拟合
np.random.seed(42)
ages = np.random.normal(35, 8, 10000).astype(int); ages = np.clip(ages,18,65)

fig, ax = plt.subplots(figsize=(10,6))
ax.hist(ages, bins=25, density=True, alpha=0.7, color='skyblue', edgecolor='black')
x = np.linspace(15,65,100)
ax.plot(x, norm.pdf(x,35,8), 'r-', lw=3, label='正态拟合')
ax.set_title('平台用户年龄分布（N=10,000）', fontsize=16, fontweight='bold')
ax.legend(); plt.tight_layout();
plt.show()