import numpy as np

a = np.arange(12)
b = a.reshape(3, 4) # 重塑
c = b.ravel() # 展平
d = b.T # 转置
e = np.newaxis # 增加维度神器
# 例子：(100,) → (100, 1)
x = x[:, np.newaxis]


