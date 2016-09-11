__author__ = 'Yui'

def find_x(a):
    x = raw_input('input')
    print(x)
    n = 0
    index = 0
    print(len(x))
    while index < len(x):
        if x[index] == a :
            print(x[index])
            return n+1
        else:
            return n
        index = index + 1

find_x('a')


