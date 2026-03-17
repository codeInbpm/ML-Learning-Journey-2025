import numpy as np
import matplotlib.pyplot as plt
# 如果是中文环境，加这行防止乱码
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
data = np.random.randn(1000)
