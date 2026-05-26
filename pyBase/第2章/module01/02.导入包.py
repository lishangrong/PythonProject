"""
包：本质就是一个文件夹，该文件夹中可以包含若干个python模块(.py文件),文件夹下还包含了一个__init__.py
   作用：模块文件较多时，用来管理多个模块。（包的本质也是一个模块）
包的导入方式：
1. import 包名.模块名 / import utils.my_fun / utils.my_fun.log_separator1()
2. from 包名 import 模块名 / from utils import my_fun / my_fun.log_separator1()
3. from 包名 import * / from utils import * / my_fun.log_separator1()
4. from 包名.模块名 import 功能名 / from utils.my_fun import log_separator1()  / log_separator1()
5. from 包名.模块名 import *  / from utils.my_fun import *  / log_separator1()
注意：使用【from 包名 import *】时，需要在__init__.py 文件中添加 __all__=[]
"""