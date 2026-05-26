"""
网络机器人：也称为网络爬虫，是一种按照一定的预设规则，自动浏览并抓取网络数据的程序或脚本。
开始 ---> 发送HTTP请求 ----> 解析结果并提取数据 -----> 数据处理(清洗) ----> 数据存储 ----> 结束

数据清洗：是指对采集到的原始数据进行处理、修正、转换和标准化的过程，目的是让数据变的规范、准确。

网络机器人-合规性（robots协议）
robots 协议也称为爬虫协议、爬虫规则，
是指网络根目录下存放的一份文本文件 robots.txt，用于告诉爬虫哪些页面可以抓取，哪些页面不能抓取。（君子协议）
User-Agent:用户代理，通过该请求头确认爬虫的类型
Disallow：禁止访问的资源
Allow：允许访问的资源
Sitemap：网站地图，帮助爬虫更搞笑地获取网站内容
Crawl-delay：爬取间隔时间，避免频繁访问造成网站压力过大

百度网站-网络机器人协议文档：https://www.baidu.com/robots.txt
eqxiu:  https://www.eqxiu.com/robots.txt


需求：获取TIOBE 编程语言排行榜单（https://www.tiobe.com/）
1. 查看 TIOBE 网站的 robots.txt， 明确资源获取的规则
2. 安装 requests库，用于发送网络请求(pip install requests)
3. 编写python代码， 访问TIOBE网站，获取数据

"""

import requests
from lxml import html

# 1.定义url
target_url = "https://www.tiobe.com/tiobe-index/"
# 2.发送请求，获取数据
response = requests.get(target_url)

document = html.fromstring(response.text)
# 3.解析数据
# 3.1 解析表头
# th_list = document.xpath("//table[@id='top20']/thead/tr/th/text()")
# th_list = document.xpath("/html/body/section/div/article/table[1]/thead/tr/th/text()")
th_list = document.xpath("//*[@id='top20']/thead/tr/th/text()")
print(th_list)
# 3.2 解析数据
tr_list = document.xpath("//table[@id='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)


