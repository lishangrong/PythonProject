"""
网络编程介绍：
概述： 网络编程也叫网络通信，Socket通信，即：通信双方都独有自己的Socket对象。
    数据在Socket 之间 通过  数据报包(UDP协议) 或者 字节流(TCP协议) 的形式进行传输

socket 常用于服务器端的函数
bind(address): 绑定地址(host,port) 到socket套接字，
    在AF_INET下，address以元祖(host,port)的形式表示地址。
    参数host表示字符串类型的主机名或ip地址；port表示int类型的端口号
listen(backlog): 开始TCP监听，参数backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。
                    该值至少为1，大部分应用程序谁5就可以了，最大值可设置为128
accept(): 被动接受TCP客户端连接，等待连接的到来，返回一个connection对象，以元祖形式显示，
            且元祖的第一个参数为已经建立连接的socket对象，第二个参数为地址address

同时应用于服务器端和客户端的函数：
recv(bufsize): 用于接收TCP数据，数据以bytes二进制形式返回，bufsize指定要接收的最大数据量，可设置为1024
send(data)：发送TCP数据，将data中的数据发送到连接的socket，data为bytes二进制数据
close(): 关闭socket
setsocketopt(level, optname, value):可设置端口号复用，让程序退出端口号并立即释放。
        level可指定为SOL_SOCKET，optname可指定为SO_REUSEADDR，value可指定为True

"""

import socket

# 创建socket
# 参1：AddressFamily 地址族，即：Ipv4 还是 Ipv6 默认值：AF_INET(ipv4), AF_INET6(ipv6)
# 参2：SocketType Socket类型，即：TCP 还是 UDP 默认值：SOCK_STREAM(TCP), SOCK_DGRAM(UDP)
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
