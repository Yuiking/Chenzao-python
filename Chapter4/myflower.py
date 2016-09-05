from __future__ import print_function, division

import turtle
from basic import arc

def petal(t,r,angel):
    for i in range(2):
        arc(t,r,angel)
        t.lt(180-angel)

def flower(t,n,r,angle):
    for i in range(n):
        petal(t,r,angle)
        t.lt(360.0/n)

bob = turtle.Turtle()

flower(bob,8,100,80)


# wait for the user to close the window
turtle.mainloop()

