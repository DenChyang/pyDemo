#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/01/01 19:57
# @Author  : DengQiang.Wu
# @File    : 01_static_web_server.py

# 创建tcp socket服务器
# TODO:最后一课没看完，代码没写完
import socket
from multiprocessing import Process

HTML_ROOT_DIR = ""


def handle_cli(cli_socket):
    """
    处理客户端请求
    :param cli_socket:
    :return:
    """
    # 接收数据
    request = cli_socket.recv(1024)
    # request_data = recv()
    print("request:",request)
    # print(request_data)
    # 解析HTTP报文数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_srart_headers = "Server: my server\r\n"
    response_body = "this is my server"
    response = response_start_line + response_srart_headers + "\r\n" + response_body
    print("response:",response)
    cli_socket.send(bytes(response,"utf-8"))
    # 因为是多进程，所以需要关闭进程中的资源
    cli_socket.close()

    # 提取请求方式
    # 提取请求路径
    # 返回响应数据
    # send()
    # close()


def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1",8000))
    server_socket.listen(128)

    while True:
        cli_socket, cli_addr = server_socket.accept()
        print("[%s,%s]"%cli_addr)
        handle_cli_process = Process(target=handle_cli,args=(cli_socket,))
        handle_cli_process.start()
        cli_socket.close()


if __name__ == '__main__':
    main()


