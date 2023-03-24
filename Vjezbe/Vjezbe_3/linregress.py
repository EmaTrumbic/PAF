import matplotlib.pyplot as plt
import numpy as np
import math
M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #mjerna jednica Nm
kut = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #mjerna jedinica rad

umnozak_kut_M = 0
suma_kvadrata_kut = 0
suma_kvadrata_M = 0

for i in range(len(M)):
    umnozak_kut_M += kut[i]*M[i]
    suma_kvadrata_kut += (kut[i])**2
    suma_kvadrata_M += (M[i])**2

umnozak_srednja_vr = umnozak_kut_M / len(M)
kut_kvadrat_srednja_vr = suma_kvadrata_kut / len(kut)
M_kvadrat_srednja_vr = suma_kvadrata_M / len(M)

print('Vrijednosti dobivene koristeci formule iz zadatka:')
Dt = umnozak_srednja_vr / kut_kvadrat_srednja_vr
print('Modul torzije = {}'.format(Dt))
stand_devijacija = math.sqrt(((M_kvadrat_srednja_vr/kut_kvadrat_srednja_vr)-Dt**2)/len(M))
print('Standardna devijacija = {}'.format(stand_devijacija))

print('Vrijednosti dobivene pomocu polyfit-a:')
print('Modul torzije = {}'.format(np.polyfit(kut, M, deg=1)[0]))
print('Standardna devijacija = {}'.format(np.polyfit(kut, M, deg= 1)[1]))

y = []
for el in kut:
    y.append(el * np.polyfit(kut, M, deg=1)[0])

plt.plot(kut, M, 'go')
plt.plot(kut, y)
plt.xlabel('Kut [rad]')
plt.ylabel('M [Nm]')
plt.show()
