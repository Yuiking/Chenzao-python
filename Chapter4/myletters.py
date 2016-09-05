import turtle
from basic import arc,square,polyline


def square(t, length):
    """Draws a square with the given length.
    :param t: Turtle
    :param length: Side length
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

def Forward_slash(t,length,angle):
    t.lt(angle)
    t.fd(length)

def Back_slash(t,length,angle):
    t.lt(180-angle)
    t.fd(length)

