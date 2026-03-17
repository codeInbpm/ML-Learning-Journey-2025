# ML-Learning-Journey-2025

🚀 **2025 机器学习・深度学习・大模型全路线学习之旅**  
> 本仓库记录从零基础到精通的完整学习路径：数据处理 → 传统ML → 深度学习 → CV → NLP → 大模型 → MLOps。  
> 目标：7 天 pandas 打卡后，每周一个实战项目。仿照企业级项目结构，边学边练，边练边推。  
> 当前进度：第1天 pandas 环境搭建 + 数据探索已完成（泰坦尼克号数据集初步分析）。

---

## 系统说明
- **学习框架**：基于 Python 3.11 + Jupyter Notebook + PyTorch（主力框架）。  
- **核心路径**：实战导向，每阶段配视频资源 + 代码 notebook + Kaggle 项目。  
- **特色功能**：每日 GitHub 打卡、进度复选框、完整 EDA 报告生成、模型部署 demo。  
- **适用人群**：零基础转行 AI，从游戏数字识别项目起步，直通大模型微调。

## 安装
1. **克隆仓库**  
   ```bash
   git clone https://github.com/codeInbpm/ML-Learning-Journey-2025.git
   cd ML-Learning-Journey-2025
   ```

2. **创建虚拟环境**（推荐 conda）  
   ```bash
   conda create -n ml2025 python=3.11 -y
   conda activate ml2025
   ```

3. **安装依赖**  
   ```bash
   pip install -r requirements.txt
   ```
   （requirements.txt 已包含 pandas、numpy、matplotlib、seaborn、jupyter 等）

4. **启动 Jupyter Notebook**  
   ```bash
   jupyter notebook
   ```
   打开后，按天运行对应 notebook（如 `01_pandas_basics/day01_pandas.py`）。

## 使用
- **每日打卡流程**  
  1. 进入对应文件夹（如 `cd 01_pandas_basics`）。  
  2. 运行 notebook 或 .py 文件。  
  3. 更新 README.md（添加截图 + 心得）。  
  4. 提交 GitHub：  
     ```bash
     git add .
     git commit -m "feat: 第X天 [主题] 完成"
     git push origin main
     ```

- **数据处理示例**（第1天）  
  ```python
  import pandas as pd
  df = pd.read_csv("module1_data_foundation/data/titanic.csv")
  print(df.head())  # 探索数据
  ```

- **可视化示例**（第7天项目）  
  ```python
  import seaborn as sns
  sns.countplot(data=df, x='Sex', hue='Survived')
  plt.show()  # 性别与存活率分析
  ```

- **项目预览**（后续阶段）  
  - CV 项目：`python cv_projects/game_digit_recognition.py`（游戏截图数字识别）。  
  - 大模型：`python llm_projects/local_chatgpt.py`（Llama3 + LangChain 本地部署）。

## 核心依赖

| 依赖          | 版本     |
|---------------|----------|
| Python       | 3.11    |
| pandas       | 2.2.3   |
| numpy        | 1.26.0  |
| matplotlib   | 3.8.0   |
| seaborn      | 0.13.0  |
| Jupyter      | 1.0.0   |
| PyTorch      | 2.3.0   |  <!-- 后续阶段添加 -->
| FastAPI      | 0.110.0 |  <!-- 部署阶段 -->

## 模块说明
```
ML-Learning-Journey-2025/
├── README.md                          # 总学习计划 + 进度
├── requirements.txt                   # 环境依赖
├── data/                              # 共享数据集（titanic.csv 等）
├── 01_pandas_basics/                  # 第1阶段：pandas 基础
│   ├── day01_pandas.py                # 日志：环境搭建 + 数据读取
│   ├── README.md                      # 日志：截图 + 心得
│   └── data/                          # 阶段数据
├── 02_pandas_indexing_filtering/      # 第2阶段：索引 + 筛选
├── ...                                # 后续7天 pandas
├── ml_core/                           # 第2阶段：传统机器学习
│   ├── supervised_learning/           # 监督学习 notebook
│   └── unsupervised_learning/         # 无监督学习
├── deep_learning/                     # 第3阶段：PyTorch + 理论
├── cv_projects/                       # 第4阶段：计算机视觉（YOLO 等）
├── nlp_llm/                           # 第5-6阶段：NLP + 大模型（LangChain、RAG）
├── mlops/                             # 第7阶段：部署 + MLOps
└── docs/                              # 资源链接 + 笔记
    └── resources.md                   # 视频/文档合集
```

## 学习路线图（8阶段进度表）

| 阶段 | 主题                  | 时长 | 关键输出                  | 状态 |
|------|-----------------------|------|---------------------------|------|
| 1    | 数据工程（pandas）   | 7天  | Titanic EDA 报告 (10图)  | ✅ 进行中 |
| 2    | 传统机器学习         | 4周  | Kaggle Titanic 预测模型  | ⏳   |
| 3    | 深度学习 + PyTorch   | 3周  | MNIST 手写数字识别       | ⏳   |
| 4    | 计算机视觉 (CV)      | 4周  | 游戏截图数字识别工具     | ⏳   |
| 5    | 自然语言处理 (NLP)   | 3周  | 文本分类 + BERT 微调     | ⏳   |
| 6    | 大模型 (LLM) 实战     | 4周  | 本地 ChatGPT + RAG 系统  | ⏳   |
| 7    | 工程化 & MLOps       | 2周  | FastAPI 模型部署 demo    | ⏳   |
| 8    | 实战项目整合         | 持续  | 私人 AI 相册 + 知识库    | ⏳   |

详细计划见根目录 [高颜值路线图](README_original.md)。

## 许可证
MIT License - 自由使用、修改、分享。详情见 [LICENSE](LICENSE)。

## 贡献
欢迎 star、fork、issue！  
- 提交代码：Fork → 修改 → Pull Request（参考 `CONTRIBUTING.md`）。  
- 反馈学习心得：开 issue 讨论某个阶段的坑。  
- 一起打卡：@我，我们互关鼓励！

## 联系方式
- **作者**：brian
- **邮箱**：brainwang1987@gmail.com  
- **社区**：欢迎加入 QQ 群/微信群（后续添加），或在 issue 留言。  
- **Demo 预览**：后续项目上线后，会放 Colab 链接（如游戏数字识别在线 demo）。

---

⭐ **Star 这个仓库，加入 2025 AI 学习军团！**  
📈 **当前 Stars: 0 | Forks: 0 | 目标: 100 Stars 前分享第一个大模型项目**  

---
