#!/usr/bin/python
# -*- coding: UTF-8 -*-

import turtle
import math
from basic import polygon


def pie(t,n,r):
    angle = 360.0 / n
    x = angle / 2.0
    polygon(t,r,n)
    t.lt(x+90)
    t.fd(r)
    for i in range(n-1):
        t.lt(90-angle)
        t.fd(r)



bob = turtle.Turtle()
pie(bob,6,100)


# wait for the user to close the window
turtle.mainloop()
