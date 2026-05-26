"""
# 读文件 -- 方式1
# 1.打开文件
f = open("resources/望庐山瀑布.txt", "r", encoding="utf-8")
# 2.读取文件
# content = f.read() #读取所有内容
# print(content)

content_list = f.readlines()
for line in content_list:
    print(line.strip())

# 3.关闭文件
f.close()
# 读文件--方式2
with open("resources/望庐山瀑布.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
"""
"""
# 写文件
# 1. 打开文件
f = open("resources/静夜思.txt", "w", encoding="utf-8")
# 2.写入文件内容
f.write("静夜思(李白)\n\n")
f.write("窗前明月光，\n")
f.write("疑是地上霜，\n")
f.write("举头望明月，\n")
f.write("低头思故乡。")
# 3.关闭文件
f.close()
"""

"""
#  =======================  文件操作-释放资源 方式一 =========================
# 写文件(写文件过程中出错，无法正常关闭文件----》 try--finally)
# 1. 打开文件
f = open("resources/静夜思.txt", "w", encoding="utf-8")
try:
    # 2.写入文件内容
    f.write("静夜思(李白)\n\n")
    f.write("窗前明月光，\n")
    f.write("疑是地上霜，\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。")
finally:
    # 3.关闭文件
    f.close()
"""

# ==================== 文件操作-释放资源 方式二(推荐方式，最佳实践) ===========================
# 写文件
# 1. 打开文件
with open("resources/静夜思.txt", "w", encoding="utf-8") as f:
    # 2.写入文件内容
    f.write("静夜思(唐 李白)\n\n")
    f.write("窗前明月光，\n")
    f.write("疑是地上霜，\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。")



