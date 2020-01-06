#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/01/05 15:07
# @Author  : DengQiang.Wu
# @File    : 01.面试题.py

class Foo(object):
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item,end=" ")
        return self

    def __str__(self):
        return ""


if __name__ == '__main__':

    print(Foo().hello.different.green)