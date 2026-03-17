
### 一、 数据预处理与清洗（最常用）
这是业务开始前最耗时、也最关键的步骤。

| 方法 | 业务场景 | 核心参数 | 示例代码 |
| :--- | :--- | :--- | :--- |
| **`dropna()`** | 过滤无效数据。例如：剔除没有填写手机号的潜客名单。 | `axis=0/1`, `how='any'/'all'`, `subset=['列名']` | `df.dropna(subset=['phone'])` |
| **`fillna()`** | 补全缺失值。场景：库存缺失默认为 0，或用平均分补全缺考成绩。 | `value`, `method='ffill'`(向前填充) | `df['stock'].fillna(0)` |
| **`duplicated()`** | 查找重复。场景：核查数据库中是否存在重复生成的订单 ID。 | `subset`, `keep='first'/'last'` | `df[df.duplicated('order_id')]` |
| **`replace()`** | 业务映射。场景：将“退货”、“拒收”统一归类为“未成交”。 | `to_replace`, `value`, `regex=True` | `df.replace(['退货', '拒收'], '未成交')` |
| **`rename()`** | 修改表头。场景：将导出的英文后台字段改为易读的中文报表。 | `columns={'旧名': '新名'}`, `inplace` | `df.rename(columns={'amt': '金额'})` |
| **`astype()`** | 格式修正。场景：将 Excel 读入的字符串格式金额转为浮点数进行计算。 | `dtype` (int, float, str, datetime) | `df['price'] = df['price'].astype(float)` |

---

### 二、 统计分析与数据聚合
用于生成业务报表、计算 KPI 指标。

| 方法 | 业务场景 | 核心参数 | 示例代码 |
| :--- | :--- | :--- | :--- |
| **`value_counts()`** | 频率统计。场景：统计不同省份客户的分布数量，做占比分析。 | `normalize=True`(转为百分比), `sort=True` | `df['city'].value_counts()` |
| **`groupby()`** | 维度分组。场景：按“门店”分组计算“销售总额”和“客单价”。 | `by`, `as_index=False`, `sort` | `df.groupby('shop')['amt'].sum()` |
| **`agg()`** | 多重聚合。场景：一次性算出各渠道的最高销量、最低销量和平均销量。 | 字典形式 `{'列名': ['sum', 'mean']}` | `df.groupby('cid').agg(['max', 'min'])` |
| **`pivot_table()`** | 透视表。场景：横轴为年份，纵轴为地区，展示销售额矩阵。 | `values`, `index`, `columns`, `aggfunc` | `df.pivot_table(v='sales', i='city', c='year')` |
| **`rank()`** | 业务排名。场景：计算员工销售额在部门内的排名（支持并列排名）。 | `method='dense'/'min'`, `ascending=False` | `df['rank'] = df['sales'].rank(ascending=False)` |
| **`describe()`** | 快速诊断。场景：一键查看各产品销量的均值、标准差、分位数。 | `percentiles=[.25, .5, .75]` | `df['sales'].describe()` |

---

### 三、 数据合并、变形与性能提升
用于处理多表关联及复杂的数据结构调整。

| 方法 | 业务场景 | 核心参数 | 示例代码 |
| :--- | :--- | :--- | :--- |
| **`merge()`** | 数据库联表。场景：通过 `user_id` 把“订单表”和“用户画像表”左连接。 | `on`, `how='left'/'inner'/'outer'`, `suffixes` | `pd.merge(df1, df2, on='id', how='left')` |
| **`concat()`** | 纵向堆叠。场景：将 12 个月份的月度销售明细合并成年度总表。 | `axis=0/1`, `ignore_index=True`, `join` | `pd.concat([jan, feb, mar], axis=0)` |
| **`map()` / `apply()`** | 自定义逻辑。场景：根据复杂公式计算奖金，或对证件号脱敏。 | `func` (lambda 或自定义函数) | `df['id_mask'] = df['id'].map(mask_func)` |
| **`query()`** | 链式筛选。场景：在大规模数据中筛选“上海”且“GMV > 10w”的优质商家。 | `expr` (字符串表达式) | `df.query("city == 'SH' and gmv > 100000")` |
| **`sample()`** | 随机抽样。场景：从 100 万行用户数据中抽取 5000 行做问卷调研或灰度测试。 | `n` (数量), `frac` (比例), `random_state` | `df.sample(frac=0.1)` |
| **`to_excel()`** | 结果导出。场景：将分析好的 Pandas 数据帧保存为可供业务方查看的 Excel。 | `excel_writer`, `sheet_name`, `index=False` | `df.to_excel('report.xlsx', index=False)` |

---

**💡 小技巧：**
* 如果你要处理的是**超大数据量**（千万级），建议在读取时配合 `usecols` 参数只读取需要的列，或者使用 `df.info(memory_usage='deep')` 查看内存占用。
* 遇到**时间序列分析**，请务必先用 `pd.to_datetime()` 转换日期列，这样才能直接使用 `df['date'].dt.month` 这种便捷操作。