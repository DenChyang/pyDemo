
from socket import *
import struct

udp_socket = socket(AF_INET, SOCK_DGRAM)
# udp_socket.bind(("",69))


def download(file_name,ip):
    f=open(file_name,"bw")
    pack = struct.pack("!H8sb5sb", 1, "test.jpg", 0, "octet", 0)
    udp_socket.sendto(pack,(ip,69))
    while True:
        recv_data = udp_socket.recvfrom(1024)
        if recv_data==():
            break
        else:
            f.write(recv_data[0])

    f.close()

def main():
    file_name = input("请输入要下载的文件名")
    ip = input("请输入要下载的ip地址:")
    download(file_name,ip)

if __name__ == '__main__':
    main()