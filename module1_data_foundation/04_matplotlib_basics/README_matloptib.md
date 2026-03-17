**常见子图写法**

| 方法                  | 作用（人话）                         | 常用参数 + 推荐写法（直接抄）                                                                 |
|-----------------------|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `plt.subplots()`      | 一次性创建「画布 + 坐标轴」，专业画图必用！ | `fig, ax = plt.subplots(figsize=(10, 6))` → 一张图<br>`fig, axes = plt.subplots(2, 3, figsize=(15, 8))` → 2行3列共6张子图 |

### 常见子图写法

| 需求                   | 代码（直接复制）                                    | 说明                     |
|------------------------|----------------------------------------------------|--------------------------|
| 一张图                 | `fig, ax = plt.subplots(figsize=(10, 6))`          | 推荐！                   |
| 1行2列（左右两张图）    | `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))` | 横着放两张             |
| 2行2列（四宫格）       | `fig, axes = plt.subplots(2, 2, figsize=(10, 8))`  | axes 是 [[ax1,ax2],[ax3,ax4]] |
| 2行3列（六张子图）     | `fig, axes = plt.subplots(2, 3, figsize=(15, 8))`  | 常用监控大盘             |
记住：  
以后只要看到 `plt.plot()` 直接改成 `ax.plot()`，你就进入了 Matplotlib 职业选手行列！


[//]: # (----------------)

**真正一表在手、天下我有** 的 Matplotlib 终极速查表（工作党人手一份）  
以后画图再也不用狂搜文档了，直接在这张表里找就行！

| 类别            | 方法（推荐写法）                              | 作用（人话）                              | 必背参数 / 示例（直接抄）                                                                 |
|-----------------|----------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------|
| 创建画布        | `fig, ax = plt.subplots(figsize=(w, h))`     | 一张图最专业写法                          | `figsize=(10,6)` 控制大小                                                                 |
|                 | `fig, axes = plt.subplots(nrows, ncols)`     | 多子图一次创建                            | `fig, axes = plt.subplots(2, 3, figsize=(15,8))`                                          |
| 折线图          | `ax.plot(x, y)`                              | 最常用！画线                              | `ax.plot(x, y, 'r--', label='收益', linewidth=2)`                                         |
| 散点图          | `ax.scatter(x, y)`                           | 画点，聚类/相关性必备                     | `ax.scatter(x, y, c='red', alpha=0.6, s=50)`                                               |
| 柱状图          | `ax.bar(categories, values)`                 | 对比销量、排名                            | `ax.bar(['A','B','C'], [5,8,3], color=['#2ecc71','#e74c3c','#3498db'])`                  |
| 水平柱状图      | `ax.barh(categories, values)`                | 排名前10太长时用                          |                                                                                           |
| 直方图          | `ax.hist(data, bins=30)`                     | 看数据分布（最常用！）                    | `ax.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.8)`                 |
| 箱线图          | `ax.boxplot(data)`                           | 异常值检测、A/B测试                       | `ax.boxplot([group, 女生], notch=True, patch_artist=True)`                                  |
| 饼图            | `ax.pie(sizes, labels=labels)`               | 占比（少用，报表爱要）                    | `ax.pie([15,30,55], labels=['苹果','香蕉','橙子'], autopct='%.1f%%', startangle=90)`     |
| 热力图          | `ax.imshow(matrix, cmap='Reds')`             | 相关性矩阵、混淆矩阵                      | `ax.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)`                                       |
| 文字标题        | `ax.set_title('标题')`                       | 大标题                                    | `ax.set_title('2025年销售额', fontsize=16, fontweight='bold', pad=20)`                   |
| 坐标轴标签      | `ax.set_xlabel('X轴')` / `ax.set_ylabel('Y轴')` | 横纵轴名字                                |                                                                                           |
| 图例            | `ax.legend()`                                | 显示 label                                | `ax.legend(loc='upper left', fontsize=12, frameon=False)`                                 |
| 网格            | `ax.grid(True)`                              | 加网格，好看+好读数据                     | `ax.grid(True, linestyle='--', alpha=0.7)`                                                |
| 坐标轴范围      | `ax.set_xlim([0,10])` / `ax.set_ylim([0,1])` | 控制显示范围                              |                                                                                           |
| 双Y轴（神技）   | `ax2 = ax.twinx()`                           | 左右两个Y轴（比如价格+销量）              | `ax2.plot(x, volume, 'g-')` → 绿色线在右边Y轴                                             |
| 标注文字        | `ax.text(x, y, '文字')`                      | 在图上写字                                | `ax.text(5, 0.8, '峰值', fontsize=12, color='red')`                                       |
| 标注箭头        | `ax.annotate('这里最高', xy=(x0,y0), xytext=(x1,y1), arrowprops=dict(arrowstyle='->'))` | 重点标注                                  |                                                                                           |
| 保存图片        | `plt.savefig('xxx.png', dpi=300, bbox_inches='tight')` | 保存高清无白边                            | `plt.savefig('report.png', dpi=300, transparent=True)`                                    |
| 调整布局        | `plt.tight_layout()`                         | 防止标签被裁剪                            | 永远在 `show()` 之前加这一句                                                              |
| 美化边框        | `ax.spines['top'].set_visible(False)`        | 去掉上/右边框（现代风格）                 | 四句一起写最美：top/right 隐藏，bottom/left 变细                                          |


