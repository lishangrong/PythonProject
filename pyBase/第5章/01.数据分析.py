"""
数据分析：从一堆看似杂乱的数据中，通过数据清洗、分析、可视化等手段，
找出有价值的信息和结果，从而帮助我们解决实际问题（如：用户订单数据的分析、电影榜单数据分析、学校学生成绩分析等）
数据收集 ---> 数据清洗处理(Pandas) ----> 数据分析 ------> 数据可视化(Matplotlib)

数据清洗：指发现并纠正数据中可识别的错误的过程，包括处理缺失值、重复值、异常值，统一数据格式，保证数据的一致性。

数据清洗处理：去除重复数据，处理缺失值，处理异常值，一致性检查  ----常用库：Pandas

Jupyter Notebook
是一个局域Web网页的、交互式的编程笔记本，让你可以把代码、运行结果、图标和笔记全部都放在一个文件里（在数据分析、机器学习、教学和科研等领域的数据实验室）

Pandas 介绍：
是一个功能强大的结构化数据分析的工具集，底层是基于Numpy构建的，无论是在数据分析领域、还是大数据开发场景中都有显著的优势。
官网： https://pandas.pydata.org/
核心：DataFrame(类似表格)、Series(类似表格中的一列)

import pandas as pd
# 构造DataFrame --- 创建数据集（学员成绩）
df = pd.DataFrame([
    {"姓名":"向往", "语文":90, "数学":80, "英语":70},
    {"姓名":"小王", "语文":80, "数学":90, "英语":80},
    {"姓名":"小李", "语文":70, "数学":80, "英语":90},
])


# DataFrame 常见属性 -- index, columns, values, size, dtype, shape
# df.index.to_list() # index 索引
# df.columns.to_list() # columns 列名
# df.values.tolist()  #values 值
# df.size # size 元素个数
# df.dtypes  # 数据类型
# df.shape  # 数据维度 (行, 列)


Series
构建方式:
s = pd.Series([10, 20, 30])
s = pd.Series((10, 20, 30), index=("a", "b", "c"))
s = pd.Series({"a": 10, "b":20, "c": 30})

s.index
s.values  #获取值
s.dtype  #获取数据类型
s.size  # 获取数据个数
s.shape  #获取数据维度(行，)

数据读取和写入
基于Pandas 中提供的API，可以很方便的各类数据文件(csv、Excel、数据库、网络数据等)的读取和写入
# 读取数据 ----> read_csv
# df = pd.read_csv("data/sales.csv")
df = pd.read_csv("data/sales.csv",usecols=["订单号","产品类别","产品名称","销售数量","单价"])

# 数据处理
df["销售金额"] = df["销售数量"] * df["单价"]

# 写入数据 ----> to_csv
df.to_csv("data/sales_01.csv",index=False)

数据查看、选择及过滤
# 查看
df.head(n) : 查看前n行数据
df.tail(n) : 查看结尾n行数据
df.describe()：数值列的统计描述
df.info(): 查看数据信息（列表、非空计数、数据类型）
df.shape: 属性，查看数据维度(行数，列数)
df.columns: 属性， 产看列名
# 选择
df["列名"] / df.列名 : 操作单列
df[["列1","列2"]]: 操作多列
df.iloc[start:stop:step]：基于行号完成切片(不含stop)
df.loc[start:stop:step]: 基于索引标签完成切片(不含stop)

# 过滤
单条件: df[df["销售数量" >=10]]
单条件: df[df["产品类别"].isin(["服装","食品"])]
单条件: df[df["单价"].between(50, 200)]
多条件: &(并且)、|(或)

# 数据清洗： 指发现并纠正数据中可识别的错误的过程，包括处理缺失值、重复值、异常值，统一数据格式，保证数据的一致性。
# 2.1 缺失值处理
# df.isnull() # 查看缺失值
# 2.1.1 删除缺失值
# df = df.dropna()  # 删除有缺失值的行,返回一个新的DateFrame
# df = df.dropna(axis=1) # 删除有缺失值的列

# 2.1.2 填充缺失值
# df.fillna('---') # 填充缺失值
# df.ffill() # 填充缺失值, 填充上一行数据
# df.bfill() # 填充缺失值, 填充下一行数据


# 2.2 重复值处理
# 2.2.1 查看重复值
# df.duplicated() # 所有列的数据都一样，表示重复
# df.duplicated(subset=['订单号']) # 查看重复值(指定列的数据重复)
# 2.2.2 删除重复值 keep='first'/'last'/'false'
# first表示保留第一个，last表示保留最后一个，false表示删除所有重复值
# df.drop_duplicates(subset=['订单号'], keep='last')

# 2.3 异常值处理
# 2.3.1 查看异常值
df[df["单价"] < 0]
# 2.3.2 删除异常值
# df.drop(df[df["单价"] < 0].index)
# 2.3.3 修复异常值（单价为负数 -29）
# df["单价"] = df["单价"].abs() # 绝对值

# 2.4  数据格式转换（订单日期）
df["订单日期"] = df["订单日期"].str.replace('/', '-')

# 数据排序：在进行数据排序时，有两种排序方式，分别是：升序和降序。
而基于Pandas进行数据排序时，是可以按照多个列尽心排序的。

# 2. 排序
# 2.1 根据 销售数量 降序排序
df.sort_values("销售数量", ascending=False)
# 2.2 根据 单价 升序排序
df.sort_values("单价")
# 2.3 根据 单价 升序排序, 价格一样，再根据销售数量 降序排序
df.sort_values(["单价", "销售数量"], ascending=[True, False])
# 2.4 根据 单价 升序排序, 价格一样，再根据销售数量 升序排序
# df.sort_values(["单价", "销售数量"], ascending=True)


# 数据分组：分组操作就是把数据按照某个特征分成不同的组，然后对每个组分别进行统计计算。
分组后求和:    df.groupby('产品类别')['销售额'].sum()
分组后统计数量: df.groupby('产品类别')['销售额'].count()
分组后求最大值: df.groupby('产品类别')['销售额'].max()
分组后求最小值: df.groupby('产品类别')['销售额'].min()
分组后求平均值: df.groupby('产品类别')['销售额'].mean()
# 一次性
df.groupby('产品类别')['销售额'].agg('sum', 'count', 'max', 'min', 'mean')
分组后，销售数量之和、销售金额之和、单价-平均值
df.groupby("产品类别").agg({"销售数量": "sum", "销售金额": "sum", "单价": "mean" })



Matplotlib:是一个功能强大的数据可视化开源Python库，也是Python中使用的最多的图像绘图库，可以创建静态、动态、交互式的图表。

官网: https://matplotlib.org/
安装: pip install matplotlib

Matplotlib 图表详解
Title:标题（如：北京气温变化曲线）
Figure:画布
legend:图例
Grid:网格线
Xaxis：X轴
Xlabel: X轴标签(如：时间)
Xtick：X轴刻度
Yaxis：Y轴
Xtick_label:X轴刻度标签
Yloabel：Y轴标签(如：温度)
Ytick：Y轴刻度
Ytick_label:Y轴刻度标签

创建子图：
为了能同时展示多个图表，便于图标之间数据的直观对比和分析，更高效、更专业地组织和呈现复杂的可视化信息，通常会在一个画布上创建多个子图.
figure, axes = plt.subplots(nrow=2,ncols=2,figsize=(20,6), dpi=100)
nrow:行数
ncol:列数
获取子图对象：axes[0,0],axes[0,1], axes[1,0], axes[1,1]

折线图：plot(...) ---->适合展示趋势变化
柱状图: bar(...) ----> 适合展示数量对比
饼状图: pie(...)----> 适合展示比例构成

"""