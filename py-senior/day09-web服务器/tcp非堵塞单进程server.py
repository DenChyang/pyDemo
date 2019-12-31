# mydemo
# tcp server demo

from socket import *

def main():

    # 1.创建套接字
    tcp_server = socket(AF_INET, SOCK_STREAM)

    #2 绑定ip与端口
    tcp_server.bind(("",7788))

    tcp_server.setblocking(False)

    # 3 监听套接字
    tcp_server.listen(100)


    # 使用死循环进行循环接收tcp套接字
    while True:

        try:
            # 4 等待客户端来，接收消息
            clientSocket,clientAddr = tcp_server.accept()
            #recv = tcp_server.recv(1024)
            print(str(clientAddr))
            recv = clientSocket.recv(1024)
            print("%s"%recv.decode("gb2312"))
        except:
            pass
        else:
            recv = clientSocket.recv(1024)
            print("%s"%recv.decode("gb2312"))


if __name__ == '__main__':
    main()