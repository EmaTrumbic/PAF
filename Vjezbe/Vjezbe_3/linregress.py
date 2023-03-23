import matplotlib.pyplot as plt
import numpy as np
import math
M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #mjerna jednica Nm
φ = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #mjerna jedinica rad

umnozak_φM = 0
suma_kvadrata_φ = 0
suma_kvadrata_M = 0

for i in range(len(M)):
    umnozak_φM += φ[i]*M[i]
    suma_kvadrata_φ += (φ[i])**2
    suma_kvadrata_M += (M[i])**2

umnozak_srednja_vr = umnozak_φM / len(M)
φ_kvadrat_srednja_vr = suma_kvadrata_φ / len(φ)
M_kvadrat_srednja_vr = suma_kvadrata_M / len(M)

Dt = umnozak_srednja_vr / φ_kvadrat_srednja_vr

print(Dt)

stand_devijacija = math.sqrt(((M_kvadrat_srednja_vr/φ_kvadrat_srednja_vr)-Dt**2)/len(M))

print(stand_devijacija)

x = [0, 1.1]
y = []

for el in x:
    y.append(Dt*el)

plt.plot(φ,M, 'go')
plt.plot(x,y)
plt.xlabel('φ [rad]')
plt.ylabel('M [Nm]')
plt.show()