import sympy as sp
from math import cos, exp

casas = 4

def funcao(x):
    resultado = 5*x**3 + x**2 - 12*x + 4
    return round(resultado, casas)        

def derivada():
    x = sp.symbols('x')
    funcao = 5*x**3 + x**2 - 12*x + 4
    derivada = sp.diff(funcao, x)
    return derivada

def calcula_derivada(z):
    x = sp.symbols('x')
    derivada_valor = der.subs(x, z).evalf()
    return round(derivada_valor, casas)

erro = 0.01
taxa= 100.0

i1 = 1
x = i1
xn = 0

raizes = []

der = derivada()

while(taxa > 0.001): 
    xn = round(x - (funcao(x) /calcula_derivada(x)), casas)
    raizes.append(xn)
    taxa = round(abs(xn - x), casas)
    x= xn

print(raizes)

