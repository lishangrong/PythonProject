"""
该文件用作程序的入口文件
"""

from studentcms import StudentCMS

if __name__ == '__main__':
    # 1. 创建学生管理系统对象
    stu_cms = StudentCMS()
    # 2. 启动程序即可
    stu_cms.start()
