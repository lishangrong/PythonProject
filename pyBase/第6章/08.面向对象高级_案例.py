"""
基于面向对象的编程思想，完成如下系统开发
某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。
系统中有两种类型的会员：普通会员和VIP会员，他们的借书权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。
核心功能：
1.会员登录：会员通过卡号和密码登录系统
2.借书：会员可以借阅库存中有余量的图书
3.还书：会员可以归还借阅的图书
4.查看我的借阅：展示当前会员已经借阅的图书列表
5.退出系统
借阅规则：
1.普通会员最多可借3本
2.VIP会员最多可借6+VIP等级 本(VIP等级，默认为1)
注意：
1.登录成功(卡号和密码均正确)后，才可以访问该系统
2. 图书库存不足或当前会员借书数量达到最大借书数量，不能再借新书
"""
from abc import ABC, abstractmethod
import json

# 图书
class Book:
    def __init__(self, book_id, title, author, stock):
        self.book_id = book_id #编号
        self.title = title # 标题
        self.author = author # 作者
        self.stock = stock # 库存
        self.__available_num = stock # 可用数量

    #  借书
    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        else:
            return False
    #  还书
    def return_book(self):
        self.__available_num += 1

    def get_available_num(self):
        return self.__available_num

# 抽象类：是一种只能被继承，不能被实例化的类，作用就是规定子类必须要实现哪些方法，强制子类必须遵守统一的代码规范
# Python 中的抽象类，使用继承abc模块 中的ABC类 --->ABC: Abstract Base Class
# 会员类
class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id # 会员编号
        self.name = name # 姓名
        self.__password = password # 密码
        self.__borrowed_books = [] # 借阅的图书列表

    # 会员借书
    def borrow_book(self, book:Book):
        # 判断当前会员借阅数量是否达到最大限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print(f"{self.name}，您已经达到最大借阅数量，无法再借书")
            return False
        # 判断书籍是否可以借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name}已成功借阅了图书《{book.title}》")
            return True
        else:
            return False

    def return_book(self, book:Book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name}已成功归还了图书《{book.title}》")
        else:
            print(f"{self.name}，您没有借阅过图书《{book.title}》")

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books

    #  获取会员最大借阅数量(需要在子类中实现)
    @abstractmethod
    def get_max_books(self) -> int:
        pass

# 普通会员
class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3

# VIP 会员
class VIPMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level

    def get_max_books(self) -> int:
        return 6 + self.vip_level




# 图书管理系统
class LibrarySystem:
    def __init__(self):
        self.books = {} # 图书列表 {"AI001": Book对象, "AI002": Book对象}
        self.members = {} # 会员列表{"N001": Member对象}
        self.login_member: Member|None = None # 当前登录的会员
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        # 加载data/books.json数据
        with open("data/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book["编号"]] = Book(book["编号"], book["标题"], book["作者"], book["数量"])
            print("加载书籍数据成功!")

    def load_members_data(self):
        # 加载data/members.json数据
        with open("data/members.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)
            for member in members_data:
                if member["卡号"].startswith("N"):
                    self.members[member["卡号"]] = NormalMember(member["卡号"], member["姓名"], member["密码"])
                elif member["卡号"].startswith("V"):
                    self.members[member["卡号"]] = VIPMember(member["卡号"], member["姓名"], member["密码"], member["会员等级"])
            print("加载会员数据成功!")

    def login(self):
        while True:
            print("\n【登录】")
            member_id = input("请输入会员卡号：")
            password = input("请输入会员密码：")
            # 登录
            if member_id in self.members:
                member = self.members[member_id]
                if member.get_password() == password:
                    print(f"登录成功，欢迎您，{member.name}！")
                    self.login_member = member
                    return True
                else:
                    print("登录失败，密码错误！")
                    continue
            else:
                print("登录失败，会员卡号不存在！")
                continue

    def borrow_book(self):
        # 1.展示当前图书馆的图书列表
        for book in self.books.values():
            print(f"编号：{book.book_id}，标题：{book.title}，作者：{book.author}，库存：{book.stock}，可用：{book.get_available_num()}")
        # 2.获取用户输入的图书编号,执行借书动作
        book_id = input("请输入要借阅的图书编号：")
        if book_id not in self.books:
            print("图书编号不存在！")
            return

        book = self.books[book_id]
        self.login_member.borrow_book(book)

    def return_book(self):
        # 1.展示当前会员的借阅列表
        print("【已经借阅的图书列表：】")
        for book in self.login_member.get_borrowed_books():
            print(f"编号：{book.book_id}，标题：{book.title}")
        # 2.获取用户输入的图书编号,执行还书动作
        book_id = input("请输入要归还的图书编号：")
        if book_id not in self.books:
            print("图书编号不存在！")
            return
        book = self.books[book_id]
        self.login_member.return_book(book)

    def view_borrowed_books(self):
        borrowed_books = self.login_member.get_borrowed_books()
        print("【已经借阅的图书列表：】")
        if len(borrowed_books) > 0:
            for book in self.login_member.get_borrowed_books():
                print(f"编号：{book.book_id}，标题：{book.title}")
        else:
            print("您没有借阅任何图书！")

    def run(self):
        if self.login():
            while True:
                print("\n1.借阅图书")
                print("2.归还图书")
                print("3.查看借阅")
                print("4.退出系统")
                choice = input("请选择操作(1-4)：")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.view_borrowed_books()
                    case "4":
                        print("退出系统,Bye Bye~")
                        break
                    case _:
                        print("无效的选择，请重新选择！")



if __name__ == "__main__":
    ls = LibrarySystem()
    ls.run()