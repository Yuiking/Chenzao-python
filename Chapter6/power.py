#!/usr/bin/python
# -*- coding: UTF-8 -*-

def is_power(a,b):
    if b == 0:
        return False
    elif b == 1 :
        if a == 1:
            return True
        else:
            return False
    elif a/b == 1:
        return True
    elif a%b != 0:
        return False
    elif a%b == 0:
        print ('returning ')
        print (a/b, b)
        return is_power(a/b,b)


print is_power(125,5)
print is_power(9,1)