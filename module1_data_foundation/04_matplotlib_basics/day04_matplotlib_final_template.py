import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 6))

# ================== 造数据（这一段必须有！）====================
x = np.linspace(0, 10, 200)      # 0~10 之间取 200 个点
y = np.sin(x)                   # 正弦
y2 = np.cos(x)                   # 余弦
# =====================================

# 这里改你的画图代码
ax.plot(x, y, label='数据', color='#e74c3c', linewidth=2)

# 这里改标题
ax.set_title('2025年关键指标趋势', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('日期')
ax.set_ylabel('数值')
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# 美化（四句背会）
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig('result.png', dpi=300, bbox_inches='tight')  # 保存
plt.show()