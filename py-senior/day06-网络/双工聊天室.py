from threading import Thread
from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
send_ip = "127.0.0.1"
send_port = 7788
udpSocket.bind(("", 6789))
def send_content():
    """
    发送数据
    :return:
    """
    while True:
        send = input("<<")
        udpSocket.sendto(send.encode("gb2312"),(send_ip,send_port))

def recv_content():
    """
    接收数据
    :return:
    """
    while True:
        recv_msg = udpSocket.recvfrom(1024)
        content,ip_info =recv_msg
        print("[%s]:%s"%(ip_info,content.decode("gb2312")))

def main():

    send = Thread(target=send_content)
    send.start()

    recv = Thread(target=recv_content)
    recv.start()

    send.join()
    recv.join()

if __name__ == '__main__':
    main()
