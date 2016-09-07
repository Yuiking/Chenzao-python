#!/usr/bin/python
# -*- coding: UTF-8 -*-

#比较x,y的大小
def compare_value(x,y):
    if x < y:
        return -1
    if x == y:
        return 0
    if x > y:
        return 1

print compare_value(0,9)