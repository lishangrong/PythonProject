
"""
lxml: 是一个高性能的HTML/XML文档的解析库，支持基于Xpath语法来解析和获取网页数据
安装：pip install lxml
Xpath：是一种用于在HTML/XML文档中导航或定位元素的查询语言，让你能够准确的定位文档中的特定元素、属性或文本。
表达式                描述                             样例
/                从根节点的直接子元素                    /html/body/div/h1
//               从任意位置选择节点                     //h1
.                从当前节点下查找                       ./a 与 .//a
[n]              选择第n个元素                         //p[2]
[last()]         选择最后一个元素                       //p[last()]
[@attr]          选择有该属性的元素                     //p[@color]
[@attr='value']  选择该属性值等于指定值的元素             //p[@color='red']
*                匹配任何元素节点                      //body/div/*
@*               匹配元素的任何属性                    //body/div/a/@*
text()           获取文本内容                         //div/p/text()
"""
from lxml import html
from tqdm.contrib.discord import tqdm_discord

with open("resources/index.html", "r", encoding="utf-8") as f:
    html_doc = f.read()
    # 捷信html的文本，将其转换为一个文档对象
    doc = html.fromstring(html_doc)
    # 解析表头 - xpath语法
    th_list = doc.xpath("//table/thead/tr/th/text()")
    print(th_list)

    # 解析表格中的数据 - xpath语法
    # 获取第一行数据 // 表示从任意位置开始匹配
    # td_list = doc.xpath("//table/tbody/tr[1]/td/text()")
    # / 表示从根节点(html)开始
    # td_list = doc.xpath("/html/body/table/tbody/tr/td/text()")
    # print(td_list)

    # tr_list = doc.xpath("//table/tbody/tr")
    # for tr in tr_list:
    #     td_list = tr.xpath("./td/text()")
    #     print(td_list)

    # tr[2]
    td_list = doc.xpath("//table/tbody/tr[2]/td/text()")
    print(td_list)
    # last()
    td_list = doc.xpath("//table/tbody/tr[last()]/td/text()")
    print(td_list)

    print("===================================================")

    # p[@class]:表示匹配class属性为p的标签
    p_list = doc.xpath("//p[@class]/text()")
    print(p_list)
    # p[@class='xn']:表示匹配class属性为xn的标签
    p_list= doc.xpath("//p[@class='xn']/text()")
    print(p_list)

    print("===================================================")
    # * 表示匹配任意标签
    th_list = doc.xpath("//table/tbody/tr/*/text()")
    print(th_list)

    print("===================================================")
    # @src:表示匹配src属性
    # img_list = doc.xpath("//td/img/@src")
    # @*:表示匹配任意属性
    img_list = doc.xpath("//td/img/@*")
    print(img_list)
