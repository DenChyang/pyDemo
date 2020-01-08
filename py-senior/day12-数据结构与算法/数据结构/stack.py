# coding:utf-8

class Stack(object):
    # 栈
    def __init__(self):
        self.__list = []

    def appeng(self,item):
        self.__list.append(item)

    def pop(self,item):
        self.__list.pop()