import numpy as np
import math
def x(lista):
    print('Aritmeticka sredina: {}, standardna devijacija: {}'.format(np.average(lista),np.std(lista)/math.sqrt(len(lista)-1)))

x([2,5,3,4,3,6,8,6,3,5])