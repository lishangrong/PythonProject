# # 导入自定义模块
# import my_fun
#
# # 使用模块中的功能
# print(my_fun.PI)
# print(my_fun.NAME)
#
# my_fun.log_separator1()
# my_fun.log_separator3()


# # 导入自定义模块的功能
# from my_fun import PI, NAME, log_separator1, log_separator3
from my_fun import *

# # 使用模块中的功能
print(PI)
# print(NAME)

log_separator1()
log_separator3()