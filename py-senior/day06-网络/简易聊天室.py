from socket import *
from threading import Thread
def get_remote_content():
    """
    接收聊天信息
    :return:
    """
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(("",7788))
    while True:
        recvData = udpSocket.recvfrom(1024)
        get_content, destInfo = recvData
        print("你的%s"%get_content.decode("gb2312"))

if __name__ == '__main__':
    get_remote_content()


