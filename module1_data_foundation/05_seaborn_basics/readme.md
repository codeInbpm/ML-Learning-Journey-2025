

# 📊 Seaborn 数据可视化实战：从场景到实现

> **核心原则**：Matplotlib 负责“画出来”，Seaborn 负责“怎么美、怎么分析”。

## Seaborn 全方位解析
在 Python 数据可视化生态中，Seaborn 是兼顾“美观性”与“统计性”的核心工具，其设计初衷与使用场景紧密围绕数据分析需求，同时与底层库形成高效协作。以下从核心定义、与 Matplotlib 的关系、优势案例、数据集特性等维度展开详细说明：

## 与 Matplotlib 的关系——“底层引擎”与“高层接口”的协作

| 维度 | Matplotlib | Seaborn |
| --- | --- | --- |
| **定位**| `通用绘图“基石”（底层引擎）` | 统计可视化“高层接口”（专用工具） |
| **核心能力** | `完全控制图表像素级细节（如坐标轴刻度、图例位置、注释文本），支持任意自定义；但统计场景需手动编写大量代码（如分组绘图、计算分布）` | 专注统计场景，一键实现复杂统计图表；但极致自定义需依赖 Matplotlib 接口 |
| **依赖关系** | `Seaborn 的底层渲染完全依赖 Matplotlib（所有 Seaborn 图表最终都通过 Matplotlib 生成）` | 无法脱离 Matplotlib 独立运行，需同时导入 matplotlib.pyplot 控制显示/保存 |
| **适用场景** | `非统计类可视化（如工程图纸、自定义示意图）、图表细节微调` | 数据分析中的统计可视化（如探索数据分布、验证假设、展示分析结论） |


## Seaborn 是什么？—— 统计可视化的“优雅封装者”
Seaborn 是基于 Python 的统计数据可视化库，核心定位是“让数据分析中的可视化更简单、更美观”。它并非独立的绘图引擎，而是在 Matplotlib 基础上，针对统计场景做了高层封装，主要特点包括：

### 统计友好：内置大量专为统计分析设计的图表类型（如小提琴图、热力图、聚类图、时间序列趋势图），无需手动计算统计量即可直接可视化（如分布、相关性、分组对比）；
### 美观默认：自带 5 种预设主题（如 darkgrid、whitegrid）和科学配色方案（如 husl、Set2），默认生成的图表符合学术出版或商业汇报的审美标准，无需反复调整细节；
### Pandas 无缝集成：直接支持 Pandas DataFrame 作为输入，通过指定“列名”即可完成数据映射（如 x="列名"、hue="分组列名"），无需手动提取数据或转换格式；
### 极简 API：复杂图表（如多子图联动、分类数据对比）仅需 1-2 行代码即可实现，大幅降低统计可视化的学习成本和代码量。


# Step1 :
##  AI 打卡 Day5：Seaborn 高级可视化彻底搞透（只用自己的 train.csv）

**作者**：wáng ben  
**学习目标**：把 Matplotlib 升级成 Seaborn，一行代码出论文级统计图  
**数据来源**：只用自己的 `../data/titanic.csv`（前4天 Pandas/NumPy/Matplotlib 完全一致）

---

## Step 1：Seaborn 是什么？（建立认知）

Seaborn 是 Matplotlib 的**统计可视化高层 API**。  
优势：自动统计（均值、置信区间、相关性） + 美观默认主题 + Pandas 无缝集成。  
和 Matplotlib 关系：Seaborn 负责“统计 + 美学”，Matplotlib 负责“微调”。

**代码**（已验证）：

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

train = pd.read_csv('../../data/titanic.csv')
print(train.head())
```

# Step 2：主题与调色板设置（一键美化）
## 核心函数：sns.set_theme(style=..., palette=...)

推荐组合：darkgrid + husl（专业感最强）
whitegrid + pastel（干净报告风）
dark + Set2（酷炫黑底）

# Step 3：countplot（计数统计图）——彻底掌握
## 作用：自动统计分类变量的个数（最基础柱状图）。
## 关键参数：x=, hue=, order=, orient='h', palette=


## barplot 是什么？
- 显示**分类变量的平均值**（而不是个数）
- 自动带**误差棒**（置信区间）
- 老板最爱：生存率、平均年龄、平均票价等





根据你提供的代码文件，我为你整理了一份专门针对 **Seaborn 数据可视化核心图表** 的学习教程。这份教程重点讲解了 `countplot`（计数图）、`barplot`（条形图）和 `violinplot`（小提琴图）的功能、参数含义以及适用业务场景。

---

# 📊 Seaborn 数据可视化核心

基于经典的 **Titanic（泰坦尼克号）** 数据集，通过对比分析不同特征，掌握 Seaborn 最常用的统计绘图方法。

## 🛠️ 环境预设：风格与中文支持

在绘图之前，我们需要进行统一的初始化设置，以保证图表美观且中文不乱码。

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

# 关键修复：解决 VS Code 环境下图片不弹出的问题
matplotlib.use('TkAgg') 

# 统一主题：使用 darkgrid 风格配合 husl 调色板（推荐风格）
sns.set_theme(style="darkgrid", palette="husl")

# 中文支持：设置黑体，解决坐标轴负号显示异常
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

```


## 🚩 选图决策树（快速查阅）

| 你的需求 | 推荐图表 | 关键列需求 |
| --- | --- | --- |
| **数个数**：看看各个类别有多少人？ | `countplot` | 1 个类别列 |
| **看概率/平均值**：比较各组的平均水平（如生存率）？ | `barplot` | 1 个类别列 + 1 个数值列 |
| **看分布密度**：想看数据在哪里最集中？是否有极端值？ | `violinplot` | 1 个类别列 + 1 个数值列 |
| **看相关性**：哪些指标之间有因果或关联？ | `heatmap` | 多个数值列的相关系数 |
| **看相关性：哪些指标之间有因果或关联？** | `jointplot` | 同时看散点关系与各自分布 |


---

## 一、 计数统计图 `countplot`

**场景**：初步探索数据分布。例如：一等舱到底有多少人？哪个港口上船的人最多？

* **功能**：自动对类别进行计数（Frequency）。
* **常用参数**：
* `x` / `y`：类别字段。
* `hue`：**分类对比**。如按性别区分舱位人数。
* `order`：**手动排序**。如 `order=['S', 'C', 'Q']` 强制港口显示顺序。


* **代码核心**：`sns.countplot(data=train, x="Pclass", hue="Sex")`

---

## 二、 平均值条形图 `barplot`

**场景**：展示核心业务指标。例如：哪种性别的生存率更高？不同舱位的平均票价是多少？

* **功能**：计算均值（Mean）并展示**置信区间（误差棒）**。
* **常用参数**：
* `y`：必须是数值列（Seaborn 会自动算它的平均值）。
* `ci`：置信区间。设为 `None` 可隐藏误差棒，使图表更清爽。


* **注意**：`y` 轴如果是 0-1 变量（如 Survived），结果直接代表**概率**。
* **代码核心**：`sns.barplot(data=train, x="Pclass", y="Survived")`

---

## 三、 小提琴图 `violinplot`

**场景**：深入研究数据特征。例如：幸存者的年龄分布是否比遇难者更低？票价是否有明显的两极分化？

* **功能**：结合了箱线图和密度图，展示数据的**全貌（分布形状）**。
* **常用参数**：
* `split=True`：**进阶必备**。将 `hue` 的两个类别左右合体，对比感极强。
* `inner='quart'`：在内部画出四分位数线。
* `scale='count'`：根据该组人数多少调整小提琴宽度。


* **代码核心**：`sns.violinplot(data=train, x="Pclass", y="Age", hue="Survived", split=True)`

---

## 四、 热力图 `heatmap`

**场景**：多维度关联分析。例如：年纪大的人是不是票价买得更贵？哪些特征对生存影响最大？

* **功能**：将数值矩阵（通常是相关系数）映射为颜色深浅。
* **常用参数**：
* `annot=True`：在格子里标出具体数字。
* `cmap`：调色板。推荐 `RdBu_r`（红蓝，适合看正负相关）或 `YlGnBu`（黄绿蓝）。
* `fmt='.2f'`：数字保留两位小数。


* **代码核心**：`sns.heatmap(train.corr(), annot=True, cmap='coolwarm')`

---

## 💡 开发提示（必看）

1. **中文适配**：记得加 `plt.rcParams['font.sans-serif'] = ['SimHei']`。
2. **强制弹出**：VS Code 用户建议在代码最上方加 `matplotlib.use('TkAgg')` 以免窗口不显示。
3. **组合拳**：通常先用 `heatmap` 找关系，再用 `barplot` 看具体比例，最后用 `violinplot` 看细分分布。

---
