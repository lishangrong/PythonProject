# 导入模块
# import utils.my_fun
# utils.my_fun.log_separator1()
# utils.my_fun.log_separator2()
#
# from utils import my_fun, my_var
# my_fun.log_separator1()
# my_fun.log_separator2()
# my_fun.log_separator3()

# 如果要通过 from utils import * 导入包下的所有模块，需要在__init__.py 文件中添加 __all__
# from utils import *
# my_fun.log_separator1()
# print(my_var.NAME)
# print(my_var.PI)

# 导入模块中的功能
# 相对路径
from utils.my_fun import log_separator3, log_separator4
# 绝对路径
# from 第2章.utils.my_fun import log_separator3, log_separator4
log_separator4()
log_separator3()

# from utils.my_fun import *
# log_separator1()
# log_separator2()
