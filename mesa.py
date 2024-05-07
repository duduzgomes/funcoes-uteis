import numpy as np
import cramer as cm
import obterDados as od

x = [1,2,4,6]
y = [5,3,1,0.5]

a, b = od.linear(x,y)
a = np.array(a)

resultado = cm.cramer(a, b)
print(resultado)
