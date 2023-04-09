import numpy as np

def point_derivation(f, x, dx, use2PointMethod=False):
    if use2PointMethod == True:
        return (f(x+dx)-f(x))/dx
    else:
        return (f(x+dx)-f(x-dx))/(2*dx)

def list_derivation(f, a, b, dx, use2PointMethod=False):
    lista_tocaka = np.arange(a, b, dx); lista_derivacija = []
    if use2PointMethod == True:
        for x in lista_tocaka:
            lista_derivacija.append((f(x+dx)-f(x))/dx)
    else:
        for x in lista_tocaka:
            lista_derivacija.append((f(x+dx)-f(x-dx))/(2*dx))
    return lista_tocaka, lista_derivacija

def integration(f, a, b, n):
    lista = np.linspace(a, b, n); donji_int = 0; gornji_int = 0
    dx = lista[1]-a
    for x in range(len(lista)-1):
        donji_int += f(lista[x])*abs(dx); gornji_int += f(lista[x+1])*abs(dx)
    return donji_int, gornji_int

def trapezoidal_integration(f, a, b, n):
    lista = np.linspace(a, b, n); integral = 0
    dx = lista[1]-a
    for x in range(len(lista)-1):
        integral += (f(lista[x])+f(lista[x+1]))*abs(dx)/2
    return integral
