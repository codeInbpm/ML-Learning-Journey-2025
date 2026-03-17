# 把“销售额”和“库存”两张表按日期对齐合并
import pandas as pd

# 销售额表
sales = pd.DataFrame({
    "日期": ["2024-08-01", "2024-08-02", "2024-08-03"],
    "GMV": [1000, 1200, 900]
})

# 库存表
stock = pd.DataFrame({
    "日期": ["2024-08-01", "2024-08-02", "2024-08-03"],
    "库存": [200, 180, 220]
})


result = pd.concat([sales.set_index("日期")["GMV"],stock.set_index("日期")["库存"]],axis=1);
print(result)