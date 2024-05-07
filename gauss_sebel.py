import numpy as np


def calcx(y, z):
    f = 0.1 * (7 - 2*y - z)
    return (round(f,4))

def calcy(x, z):
    f = 0.2 * (-8 - x - z)
    return (round(f, 4))

def calcz(x, y):
    f = 0.1 * (6 - 2*x - 3*y)
    return (round(f, 4))

def epson(a, b):
    e = abs(a - b)
    return round(e, 4)

def epsonInteracao(a,b):
    e = a / b
    return round(e, 4)

def gaussJacobi():
    erro = 0.01
    ax= 0.7
    ay= -1.6
    az= 0.6
    taxa = 100
    ex=0
    ey=0
    ez=0

    while(taxa >= erro):
        maior_erro = 0  
        maior_valor = 0

        x = calcx(ay,az)
        y = calcy(x,az)
        z = calcz(x,y)

        ey = epson(y, ay)
        ex = epson(x, ax)
        ez = epson(z, az)

        ay = y
        ax = x
        az = z

        if(ex > ey and ex > ez):
            maior_erro = ex
        elif(ey > ex and ey > ez):
            maior_erro = ey
        else:
            maior_erro = ez

        if(x > y and x > z):
            maior_valor = x
        elif(y > x and y > z):
            maior_valor = y
        else:
            maior_valor = z

        taxa = epsonInteracao(maior_erro, maior_valor)
    
    return [x,y,z]



a = np.array([
    [1,2,4],
    [2,0,1],
    [4,2,1],
])

b = [16,8,19]

