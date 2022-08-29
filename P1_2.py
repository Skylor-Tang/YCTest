#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Skylor Tang
# @Email    : tang1996mei@126.com
# @FILE     : P1_2.py
# @Time     : 2022/8/29 16:27
# @Software : PyCharm


"""
    由于GIL的关系，Python多线程并不适合CPU密集型的计算，可以使用多进程完成
"""
from multiprocessing import Process
import time


def pf(arg):
    var = 0
    for i in range(100000000):
        var += 1
    print(arg, var)


if __name__ == '__main__':
    p1 = Process(target=pf, args=("multiprocessing_1",))
    p2 = Process(target=pf, args=("multiprocessing_2",))
    start_time = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("two process cost time: %s" % (time.time() - start_time))  # two process cost time: 4.489660978317261
    start_time = time.time()
    pf("without_multithreading_1")
    pf("without_multithreading_2")
    print("current process cost time: %s" % (time.time() - start_time))  # current process cost time: 8.43314528465271
