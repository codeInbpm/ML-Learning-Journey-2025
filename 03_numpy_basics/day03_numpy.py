import numpy as np


# 创建数组的 8 种常用方式
a = np.array([1, 2, 3, 4, 5])                  # 从 list
b = np.array([[1, 2, 3], [4, 5, 6]])           # 二维
c = np.zeros((3, 4))          # 全 0，形状 3行4列
d = np.ones((2, 3, 4))        # 全 1，三维
e = np.full((2, 3), 7)        # 全是 7
f = np.arange(0, 10, 2)       # [0 2 4 6 8]，类似 range
g = np.linspace(0, 1, 5)      # [0.   0.25 0.5  0.75 1.  ] 等间隔
h = np.random.random((3, 3))  # 随机数 [0,1)

print(a.shape)
print(b.shape)
print(a.ndim)   # a的维度
print(a.dtype) # int32还是int64
print(a.size)   # a的元素总数

print("========================")
a = np.array([[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]])

print(a[0, 1]) # 2
print(a[:, 1]) # 第1列 → [ 2 6 10]
print(a[0:2, 1:3]) # 子矩阵
print(a[a > 7]) # 布尔索引 → [ 8 9 10 11 12]
print(a[[0, 2]]) # 花式索引，取第0、2行

print("========================")

print(np.arange(10000))
print(np.arange(10000).reshape(100, 100))
print("========================")




