# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer, FunctionTransformer
import joblib
import warnings

warnings.filterwarnings('ignore')

# ====================== 1. 加载数据 ======================
df = pd.read_csv("../../data/titanic.csv")

# 数值特征列
numerical_features = ['Age', 'Fare']

X = df[numerical_features]
y = df['Survived']


# ====================== 2. 自定义异常值capping（Fare专用） ======================
def cap_outliers(X):
    X = X.copy()
    # X 可能是 DataFrame 或 numpy 数组（我们兼容两种）
    # 只对Fare做capping（Age不需要）
    if isinstance(X, pd.DataFrame):
        fare_col = 'Fare'
    else:
        fare_col = 1  # numpy 第2列就是Fare

    if 'Fare' in X.columns if isinstance(X, pd.DataFrame) else True:
        fare = X[:, 1] if isinstance(X, np.ndarray) else X['Fare']
        Q1 = np.percentile(fare, 25)
        Q3 = np.percentile(fare, 75)
        IQR = Q3 - Q1
        upper = Q3 + 1.5 * IQR
        if isinstance(X, np.ndarray):
            X[:, 1] = np.clip(fare, None, upper)
        else:
            X['Fare'] = np.clip(fare, None, upper)
    return X


# ====================== 3. 最终Pipeline（核心！） ======================
num_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),  # 第1步：缺失值中位数填充
    ('cap_outlier', FunctionTransformer(cap_outliers)),  # 第2步：Fare异常值capping
    ('binning', KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')),  # 第3步：分箱
    ('scaler', StandardScaler())  # 第4步：标准化
])

# ====================== 4. 使用方法 ======================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_transformed = num_pipeline.fit_transform(X_train)
X_test_transformed = num_pipeline.transform(X_test)

print("✅ Pipeline处理完成！")
print("训练集形状：", X_train_transformed.shape)
print("测试集形状：", X_test_transformed.shape)

# 查看前5行（Age_bin + Fare_bin + 标准化值）
print("\n新特征示例（前5行）：")
print(X_train_transformed[:5])

# ====================== 5. 保存Pipeline ======================
joblib.dump(num_pipeline, 'numerical_pipeline.joblib')
print("\n🎉 Pipeline已保存！以后加载只需：")
print("loaded_pipe = joblib.load('numerical_pipeline.joblib')")