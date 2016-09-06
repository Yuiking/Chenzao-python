__author__ = 'Yui'


def check_fermat(a,b,c,n):
    if  n <= 2:
        print "n must be big then 2!"
    else:
        if (a**n + b**n) == c**n :
            print "Holy smokes, Fermat was wrong!"
        else:
            print "No, that does not work."


a = raw_input('a=?')
b = raw_input('b=?')
c = raw_input('c=?')
n = raw_input('n=?')

check_fermat(int(a),int(b),int(c),int(n))





