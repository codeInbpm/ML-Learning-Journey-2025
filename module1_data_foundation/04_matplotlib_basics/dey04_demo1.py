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

# Demo 1：训练损失曲线
epochs = np.arange(1, 51)
train_loss = np.exp(-epochs/10) + np.random.normal(0, 0.05, 50)
val_loss = np.exp(-epochs/15) + 0.3 + np.random.normal(0, 0.08, 50)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(epochs, train_loss, 'o-', label='训练损失', color='#e74c3c', linewidth=2, markersize=4)
ax.plot(epochs, val_loss, 's--', label='验证损失', color='#3498db', linewidth=2, markersize=4)

ax.set_title('模型训练损失曲线', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('轮次 Epoch')
ax.set_ylabel('Loss')
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=12)
for spine in ['top','right']: ax.spines[spine].set_visible(False)
plt.tight_layout()
plt.show()