"""
客户端开发流程：
1. 创建客户端Socket对象
2. 连接服务器，指定服务器IP，端口号
3. 接受服务器短的信息并打印
4. 给服务器端发送消息
5. 释放资源
"""

import socket

# 1. 创建客户端Socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器，指定服务器IP，端口号
client_socket.connect(("127.0.0.1", 10086))
# 3. 接受服务器短的信息并打印
data = client_socket.recv(1024).decode("utf-8")
print(f'客户端收到的信息: {data}')
# 4. 给服务器端发送消息
client_socket.send('Socket很好玩，很有趣，我很喜欢'.encode("utf-8"))
# 5. 释放资源
client_socket.close()