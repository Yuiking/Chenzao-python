#!/usr/bin/python
# -*- coding: UTF-8 -*-


import math

signal_power = 9
noise_power = 10
ratio = signal_power % noise_power #浮点数除法
#ratio = signal_power // noise_power #地板除法
decibels = 10 * math.log10(ratio)
print(decibels)