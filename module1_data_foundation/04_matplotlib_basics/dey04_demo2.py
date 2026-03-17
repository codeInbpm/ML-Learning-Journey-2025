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


# Demo 2：销售额Top8柱状图 + 数值标签
shops = ['北京','上海','广州','深圳','成都','杭州','武汉','南京']
sales = [1258,1189,972,889,856,792,735,698]

fig, ax = plt.subplots(figsize=(10,6))
bars = ax.bar(shops, sales, color='#2ecc71', edgecolor='black')
ax.set_title('2025 Q1 店铺销售额Top8（万元）', fontsize=16, fontweight='bold', pad=20)
for i, v in enumerate(sales):
    ax.text(i, v+10, str(v), ha='center', va='bottom', fontweight='bold')
ax.grid(axis='y', alpha=0.3); plt.xticks(rotation=15)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.show()