"""
模块导入方式
1. import 模块名 / import random, os  / 模块名.功能名  random.randint(0, 10)
2. import 模块名 as 别名/  import random as rd
3. from 模块名 import 功能名/  from random import randint, choice  / randint(0, 10)
4. from 模块名 import 功能名 as 别名 /  from random import randint as rint  / rint(0, 10)
5. from 模块名 import * / from random import *  / randint(0, 10)
"""

# 导入模块 import 模块名 ---->调用方式：模块名.功能名
# import random
# import random as rd
# for i in range(100):
#     print(rd.randint(1, 100))

# 导入模块中的功能 from 模块名 import 功能名 ----> 调用方式：功能名 / 别名
# from random import randint
# from random import randint as rint
from random import *
for i in range(100):
    print(randint(1, 100))