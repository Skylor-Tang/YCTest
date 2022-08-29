#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Skylor Tang
# @Email    : tang1996mei@126.com
# @FILE     : P2.py
# @Time     : 2022/8/29 15:28
# @Software : PyCharm


"""
结论：
    Python参数传递采用的肯定是“传对象引用”的方式，
    如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值－－相当于通过“传引用”来传递对象。
    如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象。
"""


def immutable_test(v):
    v = 2
    print(f"In function, a is {v}")


def mutable_test(list_a, dict_a):
    list_a.append(2)
    print(f"In function, list_a is {list_a}")
    dict_a.update([("age", "26")])
    print(f"In function, dict_a is {dict_a}")


if __name__ == '__main__':
    a = 1
    immutable_test(a)
    print(f"In main, a is {a}")
    # In function, a is 2
    # In main, a is 1

    list_a = [1, 2, 3]
    dict_a = dict(name='tmj')
    mutable_test(list_a, dict_a)
    print(f"In main, list_a is {list_a}")
    print(f"In main, dict_a is {dict_a}")
    # In function, list_a is [1, 2, 3, 2]
    # In function, dict_a is {'name': 'tmj', 'age': '26'}
    # In main, list_a is [1, 2, 3, 2]
    # In main, dict_a is {'name': 'tmj', 'age': '26'}
