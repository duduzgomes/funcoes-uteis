def lagrange(array,a):
    def retornar_lagrange(x):
        numerador = 1
        denominador = 1
        for i in range(len(array)):
            if(i == a):
                continue
            numerador *= (x - array[i])    
        for i in range(len(array)):
            if(i == a):
                continue
            denominador *= (array[a] - array[i]) 

        resultado = numerador / denominador

        return resultado
    return retornar_lagrange

a = [0, 1, 3, 4]

l0 = lagrange(a, 0) 
l1 = lagrange(a, 1)
l2 = lagrange(a, 2)
l3 = lagrange(a, 3)

p3 =    3 * l0(3.5) + 5 * l1(3.5) + 7 * l2(3.5) + 9 * l3(3.5)
print(p3)

