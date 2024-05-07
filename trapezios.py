from math import sqrt, cos, sin

def funcao(x):
    f = sqrt(sin(x*x) + 2)
    return f

def trapezio(a,b):
    fa = funcao(a)
    fb = funcao(b)

    t = (b - a) /  2
    resultado = fa * t + fb * t

    return round(resultado, 4)

def sub_trapezio(a, b, n):
    h = (b - a) / n

    i= a + h
    s= funcao(a)

    while(i < b):
        s += 2 * funcao(i)
        i += h

    s += funcao(b) 

    resultado = h/2 * s

    return round(resultado, 4)




A = 1
B = 2
N = 4

r = sub_trapezio(A, B, N)
print(r)