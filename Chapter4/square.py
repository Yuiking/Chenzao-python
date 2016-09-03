import turtle

bob = turtle.Turtle()

def square(t,length):
    """Draws a square with the given length.
    :param t: Turtle
    :param length: Side length
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob,100)