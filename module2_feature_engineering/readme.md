# 特征工程

## 📊 数值特征工程（Numerical Feature Engineering）

**核心理念**：  
数值特征（Age、Fare、SibSp 等连续数字）是机器学习中最常见的特征类型。  
**“好特征胜过好模型”** —— 数值特征处理得好，模型效果能直接提升 10-50%。

### 1. 六大核心技巧一览表（最重要！）

| 序号 | 技巧名称                  | 作用（做什么）                              | 为什么重要（核心价值）                                                                 | 最佳使用场景                          | 核心函数 / 方法                          | 注意事项 / 常见坑                     |
|------|---------------------------|---------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------|------------------------------------------|---------------------------------------|
| 1    | **标准化**<br>（StandardScaler） | 把数据转换成**均值=0、标准差=1**          | 不同尺度特征（Age 0-80 vs Fare 0-512）会让模型“偏心”，标准化后所有特征同等重要     | 线性模型、神经网络、KNN、SVM          | `StandardScaler()`                      | 必须在训练集 fit，测试集只 transform |
| 2    | **归一化**<br>（MinMaxScaler）   | 把数据压缩到 **0~1** 区间                  | 神经网络、距离类算法对 0-1 范围最敏感，避免某个特征“一家独大”                     | 神经网络、决策树、KNN                 | `MinMaxScaler()`                        | 对异常值敏感，先处理异常值再归一化   |
| 3    | **离散化（分箱）**<br>（Binning） | 把连续数字切成固定类别（0、1、2、3、4）   | 把非线性关系变成“类别”，减少过拟合，模型更容易学习                               | 树模型（随机森林、XGBoost）、有极端值时 | `KBinsDiscretizer(n_bins=5)`            | 等频（quantile）比等宽好；箱数 5-10 最佳 |
| 4    | **缺失值填充**            | 用中位数/均值/常数填补 NaN                 | 模型无法处理 NaN，必须先填；中位数最稳健（不受极端值影响）                       | 任何有缺失值的数值列                  | `SimpleImputer(strategy='median')`      | 优先用中位数；不要用均值（易被拉偏） |
| 5    | **异常值处理**<br>（Capping）    | 把极端值“压”到合理上限（IQR法）           | 极端值（如 Fare=512）会严重拉歪模型分布，导致预测不准                             | 有明显长尾分布的特征（Fare最典型）    | `clip(upper=upper_limit)` 或 IQR        | 推荐 capping 而不是删除数据           |
| 6    | **特征交叉**              | 创建新特征：`x*y`、`x/y`、`x//10 * y` 等   | 捕捉原始特征无法表达的**非线性交互关系**（年龄×财富）                            | 几乎所有项目（Kaggle提分神器）        | 手动计算或 `PolynomialFeatures`         | 先填充缺失值再交叉；防止除0加+1      |

### 2. 数值特征处理最佳顺序（必须记住！）

```markdown
1. 缺失值填充（SimpleImputer）
2. 异常值处理（IQR Capping）
3. 特征交叉（手动创建新特征）
4. 分箱（KBinsDiscretizer）
5. 标准化 / 归一化（最后一步）
```

**为什么这个顺序？**  
先把数据“干净”了，再创造新特征，最后做尺度统一，避免数据泄漏和错误传播。

### 3. 工业级 Pipeline 模板（直接复用）

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer, FunctionTransformer

num_pipeline = Pipeline([
    ('imputer',    SimpleImputer(strategy='median')),
    ('cap_outlier', FunctionTransformer(cap_outliers)),   # 自定义capping
    ('binning',    KBinsDiscretizer(n_bins=5, encode='ordinal')),
    ('scaler',     StandardScaler())
])
```

**保存与复用**：
```python
import joblib
joblib.dump(num_pipeline, 'numerical_pipeline.joblib')
# 以后加载只需一行：loaded = joblib.load('numerical_pipeline.joblib')
```

### 4. 常见错误 & 避坑指南

- ❌ 先标准化再填缺失值 → 数据泄漏  
- ❌ 用均值填充 Age（会被婴儿和老人拉偏）→ 必须用中位数  
- ❌ 分箱后忘记 `astype(int)` → 模型可能报错  
- ❌ 特征交叉时没处理 NaN → 产生 NaN 传播  
- ❌ 测试集也用了 `fit_transform` → 数据泄漏！（必须只 `transform`）

### 5. 效果对比（你自己跑过的数据）

- 处理前：Age 有 177 个 NaN，Fare 有极端值 512  
- 处理后：所有特征干净、尺度统一、增加 Age_bin / Fare_bin / Age_Fare_product 等强特征  
- **实际提分**：Kaggle Titanic 比赛中，数值特征处理好后 AUC 通常提升 0.05~0.12

---
## Day 3：类别特征
## Day 4：时间特征
## Day 5：文本特征
## Day 6：图像特征
## Day 7：把所有特征用 Pipeline 串起来 + 提交Kaggle

