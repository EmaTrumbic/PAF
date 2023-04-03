import numpy as np

def derivation(f, x, dx, use2PointMethod):
    if use2PointMethod == True:
        return (f(x+dx)-f(x))/dx
    else:
        return (f(x+dx)-f(x-dx))/(2*dx)

def derivation2(f, a, b, dx, use2PointMethod):
    lista_tocaka = np.linspace(a, b, 40)
    lista_derivacija = []
    if use2PointMethod == True:
        for el in lista_tocaka:
            lista_derivacija.append((f(el+dx)-f(el))/dx)
    else:
        for el in lista_tocaka:
            lista_derivacija.append((f(el+dx)-f(el-dx))/(2*dx))
    return lista_tocaka, lista_derivacija

