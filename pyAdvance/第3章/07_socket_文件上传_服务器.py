"""
案例：文件上传案例，服务器端代码
回顾：网编服务器端流程
    1. 创建服务器端Socket 对象
    2. 绑定IP地址和端口号
    3. 设置最大监听数
    4. 等待客户端时间申请建立连接
    5. 读取客户端 上传的文件
    6. 释放资源
"""
import socket
# 1. 创建服务器端Socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定IP地址和端口号
server_socket.bind(("127.0.0.1", 10086))
# 3. 设置最大监听数
server_socket.listen(5)
count = 0
while True:
    count += 1
    try:
        # 4. 等待客户端时间申请建立连接
        accept_socket, client_info = server_socket.accept()
        # 5. 接收客户端上传的文件数据
        # 5.1 关联目的地文件
        with open("data/picture_" + str(count) + '.jpg', "wb") as dest_file:
            # 5.2 循环读取数据
            while True:
                # 5.3 接收客户端上传的文件数据
                bys = accept_socket.recv(8192)  # 8kb
                # 5.4 判断是否读取到数据，无数据(说明客户端断开连接)结束即可
                if len(bys) == 0:
                    break
                # 5.5 把读取到的数据写入到目的地文件中
                dest_file.write(bys)
        # # 6. 给出回执信息
        # accept_socket.send('文件上传成功'.encode("utf-8"))
    except:
        pass

# 7. 释放资源
accept_socket.close()

