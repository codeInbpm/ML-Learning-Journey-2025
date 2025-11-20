# --- day01_install_and_first_look.ipynb ---
# 标题：第1天：环境搭建 + pandas 第一次见面
# 作者：brian
# 日期：2025年11月20日

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("✅ 环境安装成功！pandas 版本：", pd.__version__)

# 1. 读取数据（把 titanic.csv 放进 data 文件夹）
df = pd.read_csv("../data/titanic.csv")    # .. 表示上一级目录

# 2. 看看长啥样
print("数据形状：", df.shape)
df.head(10)

# 3. 基本信息
df.info()
df.describe()

# 4. 看看缺失值
print("\n缺失值统计：")
print(df.isnull().sum())

# 5. 随机看几行
df.sample(5)