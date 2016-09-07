def b(z):
    print ('b',z)
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    print ('a',x,y)
    return x * y

def c(x, y, z):
    print ('c',x,y,z)
    total = x + y + z
    square = b(total)**2
    print ('square',)
    return square

x = 1
y = x + 1

print(c(x, y+3, x+y))