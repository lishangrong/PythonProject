"""
# 路径写法：(项目中，推荐相对路径写法，可移植性更好、路径简洁、易于阅读。)
1.相对路径：相当于当前工作目录的路径 ./resources/望庐山瀑布.txt   ./ 可以省略
2.绝对路径: 是从文件系统的目录开始，完整的描述文件位置的路径
# 操作模式
1. r: 只读的方式打开文件，指针放在文件的开头。（默认模式）
2. w: 只写入模式，从头编辑，原有内容会被删除；文件不存在则创建新文件
3. a:追加模式，新内容会被追加在原有内容之后；文件不存在则创建新文件

"""

# 读文件 -- 相对路径
# with open("resources/望庐山瀑布.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)

# 读文件 -- 绝对路径
with open("/Users/shangrongli/Documents/my-workspace/PythonProject/pyBase/第3章/resources/望庐山瀑布.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 写文件 a:append，追加内容， w:write,覆盖内容 ----> 文件不存在则创建
with open("resources/静夜思.txt", "a", encoding="utf-8") as f:
    f.write("静夜思(唐 李白)\n\n")
    f.write("窗前明月光，\n")
    f.write("疑是地上霜，\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n\n")
