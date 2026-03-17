import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体（防止标题乱码）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']  # Mac/Linux/Windows 都能用
plt.rcParams['axes.unicode_minus'] = False  # 负号正常显示

# ================== 造数据（这一段必须有！）====================
x = np.linspace(0, 10, 200)      # 0~10 之间取 200 个点
y1 = np.sin(x)                   # 正弦
y2 = np.cos(x)                   # 余弦
# ============================================================

# 以后画图直接复制这个模板，改数据就行
fig, ax = plt.subplots(figsize=(10, 6))   # 专业写法，推荐！！！

ax.plot(x, y1,
        label='sin(x)',
        linewidth=2,
        color='#e74c3c',
        marker='o',
        markersize=4,
        markevery=10)    # 每隔10个点画一个圆圈

ax.plot(x, y2,
        label='cos(x)',
        linewidth=2,
        color='#3498db',
        linestyle='--')

ax.set_title('正弦与余弦曲线对比', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('时间 (s)', fontsize=12)
ax.set_ylabel('幅度', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='best', fontsize=12)

# 去掉上下右边框（美观大方，论文和报表最爱）
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()   # 防止被裁剪
plt.show()