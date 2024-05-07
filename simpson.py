from math import sqrt, exp, log


def funcao(x):
    f = 3* log(x)   + (x*x)
    return round(f, 4)

def simpson(a, b):
    h = (b - a) / 2
    me = (b + a) / 2

    fa = funcao(a)
    fme = funcao(me)
    fb = funcao(b)

    resultado = h / 3 * (fa + 4*fme + fb)

    return round(resultado, 4)

def sub_simpson(a, b, n):
    h = (b - a) / (2 * n)

    s = funcao(a) 
    i = a + h
    a=0
    while(i < b):
        if(a==0):
            s += 4*funcao(i)
            a+= 1
        else:
            s += 2*funcao(i)
            a -= 1
        i += h

    resultado = h/3 * (s + funcao(b))

    return round(resultado, 4)

A = 2
B = 3
N = 2

r = sub_simpson(A, B, N)
print(r)