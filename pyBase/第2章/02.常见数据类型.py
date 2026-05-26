# 查看python 数据类型

# 1.使用内置工具type() 获取指定的字面量或变量的类型
# print(type('Hello Python'))
# print(type(10))
# print(type(3.1425))
# print(type(True))
# print(type(False))
# print(type(None))


# 2.通过 isinstance(数据, 类型) 检查数据是否属于指定的类型，返回一个bool值
print(isinstance('hello', str))
print(isinstance('hello', bool))
print(isinstance('hello', int))
print(isinstance(100, int))
print(isinstance(3.167, float))
print(isinstance(False, bool))