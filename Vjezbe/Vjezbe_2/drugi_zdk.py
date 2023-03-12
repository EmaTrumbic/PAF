import matplotlib.pyplot as plt
import numpy as np

v0 = float(input('Unesite iznos početne brzine (m/s): '))
θ = float(input('Unesite kut otklona (°): '))
θ *= 3.14159265358979323846264/180

v0x = v0 * np.cos(θ)
v0y = v0 * np.sin(θ)

x = 0
y = 0

lista_x=[0]
lista_y=[0]
t=np.linspace(0,10,10000)


for i in range(9999):
    x += v0x*0.001
    y += v0y*0.001
    v0y -= 9.81*0.001
    lista_x.append(x)
    lista_y.append(y)


fig, axes = plt.subplots(nrows=1, ncols=3)

axes[0].plot(lista_x,lista_y)
axes[0].set_xlabel('x [m]')
axes[0].set_ylabel('y [m]')
axes[0].set_title('x-y graf')

axes[1].plot(t,lista_x)
axes[1].set_xlabel('t [s]')
axes[1].set_ylabel('x [m]')
axes[1].set_title('x-t graf')

axes[2].plot(t,lista_y)
axes[2].set_xlabel('t [s]')
axes[2].set_ylabel('y [m]')
axes[2].set_title('y-t graf')

plt.show()