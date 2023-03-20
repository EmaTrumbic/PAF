import math
def funkc2(lista):
    suma1 = 0
    for el in lista:
        suma1 += el
    rez1 = suma1/len(lista)
    suma2 = 0
    for el in lista:
        suma2 += (el-rez1)**2
    rez2 = math.sqrt(suma2/(len(lista)*(len(lista)-1)))
    print('Aritmeticka sredina: {}, standardna devijacija: {}'.format(rez1,rez2))

funkc2([2,5,3,4,3,6,8,6,3,5])