import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])


print(a + b)    # [11 22 33 44]
print(a - b)    # [-9 -18 -27 -36]
print(a * b)    # [ 10  40  90 160]   ← 逐元素相乘！不是矩阵乘法
print(a / b)    # [0.1  0.1  0.1  0.1]
print(a ** 2)   # [ 1  4  9 16]       ← 幂运算
print(a < 3)    # [ True  True False False]  ← 布尔数组，神技！

print("========================")
# 标量运算

print(a + 100)   # [101 102 103 104]
print(a * 5)     # [ 5 10 15 20]
print(a <= 2)    # [ True  True False False]

print("========================")
# 广播
A = np.array([[1, 2, 3],
 [4, 5, 6]]) # (2, 3)

b = np.array([10, 20, 30]) # (3,)

A + b