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

# Demo 6：A/B测试箱线图
np.random.seed(66)
A = np.random.normal(0.085, 0.02, 1000)
B = np.random.normal(0.102, 0.025, 1000)

fig, ax = plt.subplots(figsize=(8,6))
bp = ax.boxplot([A,B], labels=['旧版','新版'], patch_artist=True, notch=True)
bp['boxes'][0].set_facecolor('#95a5a6'); bp['boxes'][1].set_facecolor('#2ecc71')
ax.set_title('A/B测试：新版转化率提升20%！', fontsize=16, fontweight='bold')
ax.set_ylabel('转化率'); ax.grid(axis='y', alpha=0.3)
plt.tight_layout(); plt.show()