import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立服务器链接
s.connect("192.168.1.250", 12354)

# 发送数据
s.send()
