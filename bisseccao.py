from math import cos, exp, sqrt, log10

def epson(a, b):
    resultado = abs((b-a)/2)
    return float(resultado)

def media(i1, i2):
    media = (i1 + i2) / 2
    return float(media)
    
def f(x):
    resultado = 4*cos(x) - exp(x)
    return resultado

erro = 0.0006

i1= 0.5
i2= 1
taxa = 100
interacoes=0
m=0

n = (log10((i2 - i1)) - log10(erro)) / log10(2)

while(taxa > erro):
    interacoes = interacoes + 1
    m = media(i1, i2)
    
    fa = f(i1)
    fb = f(i2)
    fx = f(m)

    taxa = epson(i1, i2)
    
    if(fx > 0):
        i1 = m
    else:
        i2 = m

print(round(m, 4))
print(n)
print(interacoes)
