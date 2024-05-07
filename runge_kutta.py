

def funcao(t,y):
    f = y
    return f

def rungeKutta(t, to, y, h):
    i = to
    while(i < t):
        y += (h / 2) * (funcao(i, y) + funcao(i + h, y + h * funcao(i,y) ) )
        print(y)
        i += h 

    return round(y, 4)
    

T = 4   
TO = 0
Y = 1
H = 1

r = rungeKutta(T, TO, Y, H) 
print(r)