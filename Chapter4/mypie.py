#!/usr/bin/python
# -*- coding: UTF-8 -*-

import turtle
import math


def pie(t, n, r):
    angle = 360.0 / n
    x = angle/2.0
    y = 90+x
    length = 2 * r * math.sin(x * math.pi / 180)#根据多边形半径求边长
    #由n个三角形拼接一个派
    for i in range(n):
        t.rt(x)
        t.fd(r)
        t.lt(y)
        t.fd(length)
        t.lt(y)
        t.fd(r)
        t.lt(180+x)#复位到相对初始状态


bob = turtle.Turtle()
#画出边长为100的100边形
pie(bob,100,100)

# wait for the user to close the window
turtle.mainloop()
