#!/usr/bin/python
# -*- coding: UTF-8 -*-

import turtle

def spiral(t,n, a, b):
    angle = 0
    for i in range(n):
        t.fd(4)
        step_angle = 1/(a+b*angle)
        t.lt(step_angle)
        angle += step_angle

bob = turtle.Turtle()

spiral(bob, 1000, 0.1, 0.02)
turtle.mainloop()
