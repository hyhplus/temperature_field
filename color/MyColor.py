#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
需求：
    可以提供8个通道对象，可以记录是哪个通道口、时标、温度
    提供RGB转换函数（使用变长数组的数据类型 - 列表）

"""


def color(value):
    digit = list(map(str, range(10))) + list("ABCDEF")

    if isinstance(value, tuple):
        string = '#'
        for i in value:
            a1 = i // 16
            a2 = i % 16
            string += digit[a1] + digit[a2]
        return string

    elif isinstance(value, str):
        a1 = digit.index(value[1]) * 16 + digit.index(value[2])
        a2 = digit.index(value[3]) * 16 + digit.index(value[4])
        a3 = digit.index(value[5]) * 16 + digit.index(value[6])
        tuple1 = (a1, a2, a3)
        return tuple1


if __name__ == '__main__':
    print(color("#ABABAB"))
    print(color((12, 12, 12),))
