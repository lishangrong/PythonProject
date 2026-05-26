"""
TMDB-TOP300 电影榜单数据统计分析
案例：对TMDB Top 300电影数据进行多维度统计分析并可视化展示
需求1：统计TOP300的电影中，每一年上映的电影数量的变化。(折线图)
需求2：统计对比不同语言的电影数量(柱状图)
需求3：统计对比不同类型类型数量(柱状图)
需求4：统计对比各个电影评分的比例（饼状图）
"""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import pandas as pd
from typing import Dict, List, Tuple


def load_and_clean_data(file_path: str = "data/movies.csv") -> pd.DataFrame:
    """
    加载并清洗电影数据
    
    Args:
        file_path: CSV文件路径
        
    Returns:
        清洗后的DataFrame
    """
    # 加载数据，指定需要的列和数据类型
    data = pd.read_csv(
        file_path,
        usecols=["年份", "电影名", "上映时间", "类型", "时长", "评分", "语言"],
        dtype={"年份": "Int64"}
    )
    
    # 处理缺失值：用"上映时间"的前4位填充"年份"的空值
    data["年份"] = data["年份"].fillna(data["上映时间"].str[0:4])
    
    return data


def setup_plot() -> Tuple[plt.Figure, List[List[Axes]]]:
    """
    设置图表布局和中文支持
    
    Returns:
        fig: 画布对象
        axes: 子图数组 (2x2)
    """
    # 支持中文显示
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    
    # 创建2x2的子图布局
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    
    # 添加画布标题
    fig.suptitle('TMDB-TOP300 电影榜单数据统计', fontsize=24, x=0.5, y=0.98)
    
    # 调整子图间距
    plt.subplots_adjust(hspace=0.5, wspace=0.3)
    
    return fig, ax


def plot_yearly_movie_count(data: pd.DataFrame, axes: Axes) -> None:
    """
    需求1：绘制每年电影数量变化的折线图
    
    Args:
        data: 清洗后的电影数据
        axes: 子图对象
    """
    # 分组统计每年的电影数量
    year_count = data.groupby("年份")["年份"].count()
    
    # 组装连续年份数据
    min_year = year_count.index.min()
    max_year = year_count.index.max()
    x = [i for i in range(min_year, max_year + 1)]
    y = [year_count.get(i, 0) for i in x]
    
    # 绘制折线图
    axes.plot(x, y, color="green", linewidth=2)
    axes.set_title("每年电影数量变化折线图", fontsize=18)
    axes.set_xlabel("年份", fontsize=14)
    axes.set_ylabel("数量", fontsize=14)
    axes.set_xticks(x[::10])  # X轴刻度间隔为10年
    
    # Y轴刻度间隔
    y_ticks = [i for i in range(0, 31, 3)]
    axes.set_yticks(y_ticks)
    axes.grid(linestyle="--", alpha=0.5)  # 网格线


def plot_language_distribution(data: pd.DataFrame, axes: Axes) -> None:
    """
    需求2：绘制不同语言电影数量的柱状图
    
    Args:
        data: 清洗后的电影数据
        axes: 子图对象
    """
    # 获取不同语言对应的电影数量并排序(降序)
    lang_count = data.groupby("语言")["语言"].count().sort_values(ascending=False)
    
    # 提取数据
    x_lang = lang_count.index.tolist()
    y_lang_count = lang_count.values.tolist()
    
    # 绘制柱状图
    axes.bar(x_lang, y_lang_count, width=0.7, alpha=0.5, color="green")
    axes.set_title("不同语言的电影数量柱状图", fontsize=18)
    axes.set_xlabel("语言", fontsize=14)
    axes.set_ylabel("电影数量", fontsize=14)
    axes.grid(alpha=0.5, linestyle="--")
    axes.tick_params(axis="x", rotation=45)  # 旋转x轴标签


def plot_genre_distribution(data: pd.DataFrame, axes: Axes) -> None:
    """
    需求3：绘制不同类型电影数量的柱状图
    
    Args:
        data: 清洗后的电影数据
        axes: 子图对象
    """
    # 准备数据 - 统计每种类型的电影数量
    type_count: Dict[str, int] = {}
    for types in data["类型"].str.split(","):
        for genre in types:
            if genre in type_count:
                type_count[genre] += 1
            else:
                type_count[genre] = 1
    
    # 提取数据
    x_types = type_count.keys()
    y_values = type_count.values()
    
    # 绘制柱状图
    axes.bar(x_types, y_values, width=0.7, alpha=0.5, color="orange")
    axes.set_title("不同类型的电影数量柱状图", fontsize=18)
    axes.set_xlabel("类型", fontsize=14)
    axes.set_ylabel("电影数量", fontsize=14)
    axes.grid(alpha=0.5, linestyle="--")
    axes.tick_params(axis="x", rotation=45)  # 旋转x轴标签


def plot_score_distribution(data: pd.DataFrame, axes: Axes) -> None:
    """
    需求4：绘制不同评分电影数量占比的饼状图
    
    Args:
        data: 清洗后的电影数据
        axes: 子图对象
    """
    # 获取不同评分对应的电影数量
    score_count = data.groupby("评分")["评分"].count()
    
    # 优化：小比例数据合并（比例 < 2%）归类为"其他"
    total = score_count.sum()
    threshold = total * 0.02  # 阈值2%
    
    large_scores = score_count.loc[score_count >= threshold]  # 大数据 比例 >= 2%
    small_scores = score_count.loc[score_count < threshold]
    
    if small_scores.shape[0] > 0:
        large_scores["其他"] = small_scores.sum()
    
    # 提取数据
    scores = large_scores.index.tolist()
    scores_values = large_scores.values.tolist()
    
    # 绘制饼状图
    axes.pie(scores_values, labels=scores, autopct="%1.1f%%", startangle=0)
    axes.set_title("不同评分电影数量占比饼状图", fontsize=18)
    axes.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.2))


def main():
    """主函数：执行完整的统计分析流程"""
    print("=" * 60)
    print("TMDB-TOP300 电影榜单数据统计分析")
    print("=" * 60)
    
    # 1. 加载和清洗数据
    print("\n[1/5] 正在加载和清洗数据...")
    data = load_and_clean_data()
    print(f"✓ 数据加载完成，共 {len(data)} 条记录")
    
    # 2. 设置图表布局
    print("\n[2/5] 正在设置图表布局...")
    fig, axes = setup_plot()
    print("✓ 图表布局设置完成")
    
    # 3. 绘制各个图表
    print("\n[3/5] 正在绘制每年电影数量变化折线图...")
    plot_yearly_movie_count(data, axes[0][0])
    print("✓ 折线图绘制完成")
    
    print("\n[4/5] 正在绘制语言和类型分布柱状图...")
    plot_language_distribution(data, axes[0][1])
    plot_genre_distribution(data, axes[1][0])
    print("✓ 柱状图绘制完成")
    
    print("\n[5/5] 正在绘制评分分布饼状图...")
    plot_score_distribution(data, axes[1][1])
    print("✓ 饼状图绘制完成")
    
    # 4. 保存和显示图表
    print("\n正在保存图表到 data/TMDB-TOP300.png...")
    plt.savefig('data/TMDB-TOP300.png')
    print("✓ 图表保存成功")
    
    print("\n正在显示图表...")
    plt.show()
    print("✓ 分析完成！")
    
    print("\n" + "=" * 60)
    print("统计分析结果已生成")
    print("=" * 60)


if __name__ == "__main__":
    main()
