import numpy as np

def soma(A, B, l, c):
    C= []
    for i in range(l):
        m = []
        for j in range(c):
            r = A[i][j] + B[i][j]
            m.append(r)
        C.append(m)
    return C;

def subtracao(A, B, l, c):
    C= []
    for i in range(l):
        m = []
        for j in range(c):
            r = A[i][j] - B[i][j]
            m.append(r)
        C.append(m)
    return C;

def multiplicacao(A, B, la, ca, lb, cb):
    if(ca != lb):
        print("Numero de colunas de nao e igual a de b")
        return

    C= []
    for i in range(la):
        m=[]
        for j in range(cb):
            s=0
            for k in range(ca):
                s += A[i][k] * B[k][j]
            m.append(s)
        C.append(m)
    return C




