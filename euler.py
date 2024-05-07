


def funcao(t,y):
    f = y + 1
    return f

def euler(t, to, y, h):
    i = to
    while(i < t):
        y += h * funcao(i, y)
        i += h 

    return round(y, 4)
    

T = 0.5
TO = 0
Y = 1
H = 0.1

r = euler(T, TO, Y, H)
print(r)