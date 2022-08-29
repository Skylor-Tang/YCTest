#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Skylor Tang
# @Email    : tang1996mei@126.com
# @FILE     : P3.py
# @Time     : 2022/8/29 15:42
# @Software : PyCharm

"""
    使用python标准库urllib
"""

from urllib.parse import urlparse


def parse_f(url):
    up = urlparse(url)
    hostname = up.hostname
    port = up.port
    url_path = up.path
    url_protocol = up.scheme
    print(f"域名协议：{url_protocol}\n域名：{hostname}\n端口：{port}\n路径地址：{url_path}")


if __name__ == '__main__':
    url = "http://example.com:8080/users/"
    parse_f(url)
