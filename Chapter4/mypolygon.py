import turtle
import math

bob = turtle.Turtle()

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    print(t)
    turtle.mainloop()

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    print(t)
    turtle.mainloop()

#polygon(bob,10,200)

def polyline(t,length,n,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    print (t)
    turtle.mainloop()


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, step_length,n,step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)

circle(bob,100)