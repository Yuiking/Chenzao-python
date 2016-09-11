def gcd(a,b):
    if b == 0:
       return a
    elif a%b == 0:
        return b
    elif a%b != 0:
        m = a%b
        print (b,m)
        return gcd(b,m)

print gcd(96,-13)