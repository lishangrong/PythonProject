
# csv（comma-separated value,逗号分隔值 ），是一种简单、通用的文本文件格式，用于存储表格数据，可以直接使用Excel打开。
# csv 操作---方式1
# 写
# with open("csv_data/01.csv", 'w', encoding="utf-8") as f:
#     f.write("姓名,年龄,性别,爱好\n")
#     f.write("小王,18,男,'football,Java'\n")
#     f.write("小张,19,女,basketball\n")
#     f.write("小小,21,男,running\n")
#     f.write("王王,18,男,Python\n")
#     f.write("张张,19,女,C++\n")
#     f.write("小肖,21,男,Java\n")
#     f.write("小美,18,男,化妆\n")
# 读
# with open("csv_data/01.csv", 'r', encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

# csv操作 方式二 csv(推荐)
import csv
# 写
# with open("csv_data/02.csv", 'w', encoding="utf-8", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"])
#     writer.writeheader()
#     writer.writerow({"姓名": "张三", "年龄": 19, "性别": "男", "爱好": "C++,Java"})
#     writer.writerow({"姓名": "小王", "年龄": 21, "性别": "男", "爱好": "Java"})
#     writer.writerow({"姓名": "小张", "年龄": 18, "性别": "女", "爱好": "化妆"})
#     writer.writerow({"姓名": "小小", "年龄": 21, "性别": "男", "爱好": "JavaScript"})
#     writer.writerow({"姓名": "王王", "年龄": 19, "性别": "男", "爱好": "Python"})

# 读
with open("csv_data/02.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)