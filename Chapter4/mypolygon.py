import turtle
import math


def square(t,length):
    """Draws a square with the given length.
    :param t: Turtle
    :param length: Side length
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t,length,n):
    """Draws a polygon with the given number and length.
    :param t: Turtle
    :param length: Side length
    :param n: The number of edges
    """
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def polyline(t,length,n,angle):
    """Draws a polyline with the given number,length and angle.
    :param t: Turtle
    :param length: Side length
    :param n: The number of lines
    :param angle: Angle of rotation
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)



def arc(t, r, angle):
    """Draws a arc with the given radius and angle.
    :param t: Turtle
    :param r: radius
    :param angle: Angle of rotation
    """
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


bob = turtle.Turtle()

#circle(bob,100)

#square(bob,200)

#polygon(bob,40,9)

#polyline(bob,40,6,30)


def petal(t,r,angel):
    for i in range(2):
        t.lt(angel)
        t.fd(10)
        arc(t,r,angel)
        t.rt(180-angel)

petal(bob,30,60)

# wait for the user to close the window
turtle.mainloop()