__author__ = 'Yui'

def find(a):
    x = raw_input('please write down a string.')
    print(x)
    n = 0
    for letter in x:
        if letter[n] == a:
            n = n + 1
            return n

print find('a')