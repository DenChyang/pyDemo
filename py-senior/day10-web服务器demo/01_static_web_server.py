#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/01/01 19:57
# @Author  : DengQiang.Wu
# @File    : 01_static_web_server.py

# 创建tcp socket服务器
# 完成版
import socket
import re
from multiprocessing import Process

HTML_ROOT_DIR = "D:\\mycode\\python\\pyDemo\\py-senior\\day10-web服务器demo\\resource\\"


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
    request_lines = request.splitlines()
    for line in request_lines:
        pass
    # 解析请求报文
    # GET / HTTP/1.1
    request_start_line = request_lines[0]
    # 获取用户请求的文件名-->使用正则获取
    file_name = re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode("utf-8")).group(1)
    if file_name =="/":
        file_name = "index.html"
    # 打开文件
    try:
        file = open(HTML_ROOT_DIR+file_name,"rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_srart_headers = "Server: my server\r\n"
        file_data = "404 not fount"
    else:
        # print(request_data)
        # 解析HTTP报文数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_srart_headers = "Server: my server\r\n"
        file_data = (file.read()).decode("utf-8")
        file.close()

    # response_body = "this is my server"
    response_body = file_data
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


