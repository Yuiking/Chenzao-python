from __future__ import print_function, division

from mypolygon import  arc
import turtle

bob = turtle.Turtle()

def petal(t,r,angel):
    for i in range(2):
        t.lt(angel)
        t.fd(10)
        arc(t,r,angel)
        t.rt(180-angel)

print(bob)

petal(bob,30,60)

turtle.mainloop()

