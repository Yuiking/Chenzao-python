#!/usr/bin/python
# -*- coding: UTF-8 -*-

def mysqrt(a,x):
    while True:
        y = (x + a / x) / 2.0
        if y == x :
            break
        x = y
    return y

mysqrt(2,3)





