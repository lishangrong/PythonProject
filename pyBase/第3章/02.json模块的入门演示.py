"""
读写json 格式文件：JSON是软件开发中最常用的数据交换格式，而为了简化JSON数据的处理，
在Python标准库中就提供了出库JSON数据的核心模块 json。
import json
序列化： json.dump(obj)
反序列化： json.load(f)
json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
参数：
    obj: 要序列化的对象
    fp: 文件对象
    skipkeys: 跳过无效的键
    ensure_ascii: 确保所有字符都是ASCII字符
    check_circular: 检查循环引用
    allow_nan: 允许非数字值


"""

import json

# user = {
#     "name": "小甜甜",
#     "age": 18,
#     "gender": "女",
#     "hobby": ["看电影", "听音乐", "看小说"],
#     "address": {
#         "province": "上海",
#         "city": "上海",
#         "street": "上海"
#     }
# }
# 将python对象序列化为json格式字符并写入json文件
# with open("resources/user.json", "w", encoding="utf-8") as f:
#     # ensure_ascii: 默认为True，表示所有字符都是ASCII字符， False：非ASCII码保留原样输出
#     # indent: 会在输出的json数据中添加缩进(格式化)
#     json.dump(user, f, ensure_ascii=False, indent=2)

# 读取json数据文件并反序列化json数据成字典类型
with open("resources/user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))