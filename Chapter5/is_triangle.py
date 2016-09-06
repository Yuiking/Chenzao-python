__author__ = 'Yui'

def is_triangle(x,y,z):
    if x + y <= z  or x + z <= y or y + z <= x :
        print "No"
    else:
        print "Yes"

def input():
    a = raw_input('The length of a stick = ?')
    x = int(a)
    return x

is_triangle(input(),input(),input())
