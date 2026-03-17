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

# Demo 7：2×2 监控大盘子图
fig, axes = plt.subplots(2,2,figsize=(12,9))
fig.suptitle('2025年实时监控大盘', fontsize=18, fontweight='bold')

axes[0,0].plot(np.cumsum(np.random.randn(100)+1), color='#e74c3c'); axes[0,0].set_title('QPS')
axes[0,1].fill_between(range(100), np.random.uniform(30,90,100), 70, color='orange', alpha=0.5); axes[0,1].set_title('CPU%')
axes[1,0].plot(np.random.gamma(2,2,100), color='#3498db'); axes[1,0].set_title('延迟(ms)')
axes[1,1].bar(range(100), np.random.beta(1,99,100), color='gray', alpha=0.7); axes[1,1].set_title('错误率')

plt.tight_layout(); plt.subplots_adjust(top=0.92);
plt.show()