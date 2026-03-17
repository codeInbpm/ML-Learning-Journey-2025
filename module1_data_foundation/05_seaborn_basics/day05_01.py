import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

train = pd.read_csv("../../data/titanic.csv")
print(train.head())

titanic = sns.load_dataset("titanic") # sns.load_dataset() 加载数据



print(titanic.head())

# train.csv 加载成功