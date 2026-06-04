"""
该文件用于完成 学生管理系统 的具体业务的操作，即增删改查，保存学生信息等...
"""
from student import Student
import time

# 创建学生管理系统类
class StudentCMS(object):
    # 2. 通过魔法方法init，初始化属性信息
    def __init__(self):
        # 1. 创建一个空列表，用于保存学生信息
        self.students = [] # [学生对象，学生对象，学生对象] --->[Student(...), Student(....)]
        # self.students= [
        #     Student("小王", "男", 28, "13888888888", "小王是一个爱学习，爱敲代码的小伙伴"),
        #     Student("小李", "女", 18, "13888888888", "小李是一个爱学习，爱敲代码的小伙伴"),
        #     Student("小张", "男", 66, "13888888888", "小张是一个爱学习，爱敲代码的小伙伴"),
        # ]
    # 3. 定义函数，实现答应 管理系统的界面
    @staticmethod
    def show_view():
        print("-" * 23)
        print("学生管理系统V2.0版")
        print("\t1. 添加学生信息")
        print("\t2. 删除学生信息")
        print("\t3. 修改学生信息")
        print("\t4. 查询单个学生信息")
        print("\t7. 显示所有学生信息")
        print("\t6. 保存学生信息")
        print("\t0. 退出系统")
        print("-" * 23)
        print()

    # 4. 定义函数，实现添加学生信息
    def add_student(self):
        # 4.1 提示用户输入学生信息，并接收
        name = input("请输入学生姓名：")
        sex = input("请输入学生性别：")
        age = int(input("请输入学生年龄："))
        phone = input("请输入学生手机号：")
        desc = input("请输入学生描述：")
        # 4.2 创建学生对象，并把学生信息封装到学生对象中
        stu = Student(name, sex, age, phone, desc)
        # 4.3 把学生信息添加到列表中
        self.students.append(stu)
        # 4.4 提示用户添加成功
        print(f"添加学生信息成功，学生信息为：{stu}")

    # 5. 删除学生信息
    def del_student(self):
        # 5.1 提示用户输入学生信息，并接收
        del_name = input("请输入要删除的学生姓名：")
        # 5.2 遍历列表，找到要删除的学生
        for stu in self.students:
            # 5.3 找到学生，删除学生信息
            if stu.name == del_name:
                self.students.remove(stu)
                print(f"学生 {del_name} 信息 删除成功！\n")
                break
        else:
            # 走到这里，说明没有走break，即：没有找到这个学生
            print(f"查无此人，请检查后重新删除！\n")

    # 6. 修改学生信息
    def update_student(self):
        # 6.1 提示用户输入学生信息，并接收
        upd_name = input("请输入要修改的学生姓名：")
        # 6.2 遍历列表，找到要修改的学生
        for stu in self.students:
            # 6.3 找到学生，修改学生信息
            if stu.name == upd_name:
                stu.sex = input("请输入修改后的性别：")
                stu.age = int(input("请输入修改后的年龄："))
                stu.phone = input("请输入修改后的手机号：")
                stu.desc = input("请输入修改后的描述：")
                print(f"学员 {upd_name} 信息修改成功！\n")
                break
        else:
            # 走到这里，说明没有走break，即：没有找到这个学生
            print(f"查无此人，请检查后重新修改！\n")

    # 7. 查询学生信息
    def search_one_student(self):
        # 7.1 提示用户输入学生信息，并接收
        search_name = input("请输入要查询的学生姓名：")
        # 7.2 遍历列表，找到要查找的学生
        for stu in self.students:
            # 7.3 找到学生，打印学生信息
            if stu.name == search_name:
                print(stu, end="\n\n")
                break
        else:
            # 走到这里，说明没有走break，即：没有找到这个学生
            print(f"查无此人，请检查后重新查询！\n")
    # 8. 显示所有学生信息
    def search_all_student(self):
        # 8.1 判断列表长度是否为0，如果为0， 提示:暂无学生信息，请添加后查询
        if len(self.students) == 0:
            print("暂无学生信息，请先添加后查询\n")
            return
        for stu in self.students:
            print(stu)
        print()
    # 9. 保存学生信息
    def save_student(self):
        # 9.1 关联 学生信息文件
        with open("./stu_data.txt", 'w', encoding="utf-8") as f:
            # 9.2 把[学生对象，学生对象...] --> [字典，字典...]
            stu_dict = [stu.__dict__ for stu in self.students]
            # 9.3 把字典列表写入文件
            f.write(str(stu_dict))
    
    # 10. 加载学生信息
    def load_student(self):
         # 10.1 检查文件是否存在
         try:
            # 10.2 关联学生信息文件
            with open("./stu_data.txt", 'r', encoding="utf-8") as src_f:
                # 10.3 一次性读取所有数据
                stu_data = src_f.read()           # '[字典, 字典 ....]'
                # 10.4  把上述字符串 转为列表
                stu_list = eval(stu_data)
                # 10.5 判断如果列表为空，就赋予空列表
                if len(stu_list) == 0:
                    self.students = []
                else:
                    # 10.6 把列表转为对象列表
                    self.students = [Student(**stu_dict) for stu_dict in stu_list]
         except:
             # 10.7 走这里，说明目的文件不存在，创建即可
             with open("./stu_data.txt", 'w', encoding="utf-8") as src_f:
                 pass
    # 11. 定义函数，把上述业务跑通
    def start(self):
        # 11.1 加载学生信息
        self.load_student()
        # 11.2 死循环，不断的玩
        while True:
            # 11.3 为了效果更明显，加入：延迟(休眠)
            time.sleep(1)
            # 11.4 打印 学生管理系统界面
            StudentCMS.show_view()
            # 11.5
            # 获取用户输入
            choice = input("请输入您要操作的编号：")
            # 11.6 根据用户输入的编号，做不同的操作
            match choice:
                case '1':
                    self.add_student()
                case '2':
                    self.del_student()
                case '3':
                    self.update_student()
                case '4':
                    self.search_one_student()
                case '5':
                    self.search_all_student()
                case '6':
                    self.save_student()
                    print("保存学生信息成功！")
                case '0':
                    result = input("您确定要退出系统吗？(Y/N) -->")
                    if result.lower() == 'y':
                        # 在退出前，自动保存学生数据到文件
                        self.save_student()
                        print("谢谢您的使用，期待下次再会！")
                        break
                case _:
                    print("输入有误，请重新输入")

if __name__ == '__main__':
    # scms = StudentCMS()
    # scms.show_view()
    # scms.start()
    import os
    print(os.getcwd())
