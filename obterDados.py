import numpy as np

def  linear(x,y):
    n = len(x)
    sx = 0
    sy = 0
    sx2 = 0
    sxy = 0
    x2 = []
    xy = []

    for i in range(n):
        x2.append(x[i] * x[i])
        xy.append(x[i] * y[i])
        sx2 += x2[i]
        sx += x[i]
        sy += y[i]
        sxy += xy[i]
    
    array1 = [[n,sx],
             [sx,sx2]]
    
    array2 = [sy, sxy]

    return array1, array2

def  quadratico(x,y):
    n = len(x)
    sx = 0
    sy = 0
    sx2 = 0
    sx3 = 0
    sx4 = 0
    sxy = 0
    sx2y = 0
    x2 = []
    x3 = []
    x4 = []
    xy = []
    x2y = []

    for i in range(n):
        x2.append(x[i] * x[i])
        x3.append(x[i] * x[i] * x[i])
        x4.append(x[i] * x[i] * x[i] * x[i])
        x2y.append(x2[i] * y[i])
        xy.append(x[i] * y[i])
        sx2 += x2[i]
        sx3 += x3[i]
        sx4 += x4[i]
        sx += x[i]
        sy += y[i]
        sxy += xy[i]
        sx2y += x2y[i]
    
    array1 = [[n,sx, sx2],
             [sx,sx2, sx3],
             [sx2,sx3,sx4]]
    
    array2 = [sy, sxy, sx2y]

    return array1, array2


    




