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

# Demo 5：股价 + 成交量双Y轴
dates = np.arange('2025-01-01', '2025-02-01', dtype='datetime64[D]')
price = 100 + np.cumsum(np.random.randn(31)*2)
volume = np.random.randint(5000,30000,31)

fig, ax1 = plt.subplots(figsize=(12,6))
ax1.plot(dates, price, 'g-', lw=2.5, label='收盘价')
ax1.set_ylabel('股价(元)', color='g'); ax1.tick_params(axis='y', labelcolor='g')

ax2 = ax1.twinx()
ax2.bar(dates, volume, alpha=0.3, color='gray', label='成交量')
ax2.set_ylabel('成交量(手)', color='gray'); ax2.tick_params(axis='y', labelcolor='gray')

ax1.set_title('2025年1月股票走势', fontsize=16, fontweight='bold')
fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.88))
plt.tight_layout(); plt.show()