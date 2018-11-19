#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
需求：
    传输对象：Temperature
    对象属性：温度，通道，时标，温度基准值，最高温度限制，最低温度限制
"""
import time

from RGB_store import COLOR_RGB


class Temperature:
    """

    温度： temperature
    通道： way
    时标： current_time 考虑作为类对象，无需用户输入
    温度基准值： t_base
    最高温度限制： t_max
    最低温度限制： t_min
    """
    current_time = time.time()

    def __init__(self, temperature, way, t_base, t_max, t_min):
        self.temperature = temperature
        self.way = way
        self.t_base = t_base
        self.t_max = t_max
        self.t_min = t_min

    # 静态方法不与类的实例化相关，也不关注类的对象。
    # 静态方法应用场景：临时变量的校验等。
    @staticmethod
    def static_handler():
        pass

    # 类方法有cls作为第一参数，cls是类本身对象，类对象属性需要重新赋值，因为不是实例化的对象。
    @classmethod
    def time_string(cls):
        current_time = cls.current_time
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time))
        # print(type(current_time))
        return current_time

    # 实例方法，处理温度，划分温度区间
    def temperature_handler(self):
        temperature = self.temperature
        top = self.t_max - self.t_base
        bottom = self.t_base - self.t_min

        top_div_10 = top / 10
        bottom_div_10 = bottom / 10

        if temperature >= self.t_base:
            i = int((temperature - self.t_base) / top_div_10)
            print(i)
            if i > 10:
                i = 10
            i = 10 - i
            color_ = COLOR_RGB[i][2]
            return color_

        elif temperature < self.t_base:
            j = int((self.t_base - temperature) / bottom_div_10)
            if j > 10:
                j = 10
            j = 10 + j
            color_ = COLOR_RGB[j][2]
            return color_

    # 实例化方法之间可以相互调用
    def get_temp_handler(self):
        pass

    # 实例方法，self.类的属性，直接操作类的实例化属性。
    # 这里处理颜色RGB值 -- 跟16进制（#开头）--相互转换
    def color_change(self):
        value = self.temperature_handler()
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
            tuple_ = (a1, a2, a3)
            return tuple_


# 测试方法
if __name__ == '__main__':

    t = Temperature(0, 1, 25, 100, -50)
    time_ = t.time_string()
    color = t.temperature_handler()
    color_rgb = t.color_change()

    print(time_)
    print(color)
    print(color_rgb)

    # t.get_temp_handler()


