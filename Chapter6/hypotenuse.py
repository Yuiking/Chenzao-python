#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

def hypotenuse():
    a = raw_input('the length of one side?')
    b = raw_input('the length of the other side?')
    x = int(a)
    y = int(b)
    z = math.sqrt( x**2 + y**2 )
    return z

print "%.2f" % hypotenuse()

