#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Skylor Tang
# @Email    : tang1996mei@126.com
# @FILE     : P1.py
# @Time     : 2022/8/29 15:24
# @Software : PyCharm

"""
由于GIL的关系，Python多线程并不适合CPU密集型的计算（可以使用多进程完成），Python多线程适合IO密集型的操作。
使用time.sleep()来模拟IO密集型操作
"""

import time
import threading
from functools import wraps


def timer(func_name):
    def f1(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(f"{func_name} start")
            start_time = time.time()
            func(*args, **kwargs)
            print("last time: {}".format(time.time() - start_time))
        return inner
    return f1


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)  # 模仿网络请求时，等待的过程
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")


def use_threading():
    thread1 = threading.Thread(target=get_detail_html, args=("get_detail_html",))
    thread2 = threading.Thread(target=get_detail_url, args=("get_detail_url",))
    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("last time: {}".format(time.time() - start_time))


@timer("not_use_threading")
def not_use_threading():
    get_detail_html("get_detail_html")
    get_detail_url("get_detail_url")


if __name__ == "__main__":
    use_threading()  # last time: 4.004623889923096
    not_use_threading()  # last time: 6.00872802734375
