"""
获取高分电影榜单(Top100)数据，并保存在csv文件中
数据包括：电影名、年份、上映时间、类型、时长、平分、语言、导演、作者、主演、Slogan、简介。
步骤：
1.明确网站(https://www.themoviedb.org)的robots.txt中的抓取规则
2.查看网页的结构，拆解具体的操作步骤

"""

import requests
import csv

from gitdb.util import join
from lxml import html

# 常量
MOVIE_LIST_FILE = "csv_data/movie_list.csv"
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated" #高分电影榜单的url

# 保存所有电影信息
def save_all_movie(all_movies):
    with open(MOVIE_LIST_FILE, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["电影名","年份","上映时间","类型","时长","平分","语言","导演","作者","主演","宣传语","简介"])
        writer.writeheader()
        writer.writerows(all_movies)


# 获取电影详情
def get_movie_info(movie_info_url):
    # 发送请求，获取电影详情数据
    movie_response = requests.get(movie_info_url, timeout=60)
    print(f"发送请求{movie_info_url}，获取TMDB电影榜单数据")
    # 解析数据，获取电影详情
    movie_doc = html.fromstring(movie_response.text)
    # 返回电影详情
    # 电影名称
    movie_names = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    # 上映年份
    movie_years = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    # 上映时间
    movie_dates = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()")
    # 标签
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()")
    # 时长
    movie_cost_times = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()")
    # 评分
    movie_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    # 语言
    movie_languages = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    # 导演
    movie_directors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    # 作者
    movie_authors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    # 演员阵容
    movie_actors = movie_doc.xpath("//*[@id='cast_scroller']/ol/li/p[1]/a/text()")
    # 宣传语
    movie_slogans = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")
    # 简介
    movie_descriptions = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")

    movie_info = {
        "电影名": movie_names[0].strip() if movie_names else '',
        "年份": movie_years[0].strip() if movie_years else '',
        "上映时间": movie_dates[0].strip() if movie_dates else '',
        "类型":  ",".join(movie_tags) if movie_tags else '',
        "时长": movie_cost_times[0].strip() if movie_cost_times else '',
        "平分": movie_scores[0].strip() if movie_scores else '',
        "语言": movie_languages[0].strip() if movie_languages  else '',
        "导演": ','.join(movie_directors) if movie_directors else '',
        "作者": ','.join(movie_authors) if movie_authors else '',
        "主演": ','.join(movie_actors[:-1]) if movie_actors else '',
        "宣传语": movie_slogans[0].strip() if movie_slogans else '',
        "简介": movie_descriptions[0].strip() if movie_descriptions else '',
    }
    return movie_info

# 主函数--定义核心逻辑
def main():
    # 1. 发送请求，获取高分电影榜单数据
    response = requests.get(TMDB_TOP_URL, timeout=60)
    print("发送请求，获取TMDB电影榜单数据")

    # 2. 解析数据，获取电影列表
    document = html.fromstring(response.text)
    movie_list = document.xpath("//*[@id='page_1']/div/div/div")

    # 3. 遍历电影列表，获取电影详情
    all_movies = []
    for movie in movie_list:
        movie_urls = movie.xpath("./div/div/a/@href")
        if movie_urls:
            # 电影详情的url地址
            movie_info_url = TMDB_BASE_URL + movie_urls[0]
            # print(movie_info_url)
            # 发送请求，获取电影详情信息
            movie_info = get_movie_info(movie_info_url)
            all_movies.append(movie_info)

    # 4. 保存数据，保存为csv 文件
    print("获取到所有的电影详情，保存电影数据到CSV文件.....")
    save_all_movie(all_movies)


if __name__ == '__main__':
    main()