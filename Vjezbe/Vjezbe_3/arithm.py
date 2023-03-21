import math
#Funkcija koja prima listu brojeva:
def arithm(lista):
    suma1 = 0
    for el in lista:
        suma1 += el
    arit_sredina = suma1/len(lista)
    suma2 = 0
    for el in lista:
        suma2 += (el - arit_sredina)**2
    stand_dev = math.sqrt(suma2/(len(lista)*(len(lista)-1)))
    print('Aritmeticka sredina: {}, standardna devijacija: {}'.format(arit_sredina,stand_dev))

arithm([2,5,3,4,3,6,8,6,3,5])