"""
案例：文件上传案例，服务器端代码
回顾：网编客户端端流程
    1. 创建服务器端Socket 对象
    2. 连接服务器端的IP地址和端口号
    3. 关联数据源文件，读取内容，写给服务器端
    4. 释放资源
"""

import socket

# 1. 创建服务器端Socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.  连接服务器端的IP地址和端口号
client_socket.connect(("127.0.0.1", 10086))
# 3.  关联数据源文件，读取内容，写给服务器端
with open("data/IMG117107.jpg", "rb") as f:
    while True:
        # 3.1 循环读取数据
        data = f.read(8192)
        # 3.2 判断数据长度
        if len(data) == 0:
            break
        # 3.3 发送数据
        client_socket.send(data)

# 4.  接受服务器端的反馈信息并打印
# data = client_socket.recv(1024).decode("utf-8")
# print(f'客户端收到信息: {data}')


# 5.  释放资源
client_socket.close()