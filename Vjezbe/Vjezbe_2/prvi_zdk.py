import numpy as np
import matplotlib.pyplot as plt

F = float(input('Unesite silu (N): '))
m = float(input('Unesite masu (kg): '))

a = F/m
v = 0
x = 0
akceleracija = [a]
brzina = [0]
pomak = [0]
vrijeme = np.linspace(0,10,1000)

for i in range(999):
    v += a*0.01
    x += v*0.01
    akceleracija.append(a)
    brzina.append(v)
    pomak.append(x)

fig, axes = plt.subplots(nrows=1, ncols=3)

axes[0].plot(vrijeme,pomak)
axes[0].set_title('x-t graf')
axes[0].set_xlabel('t [s]')
axes[0].set_ylabel('x [m]')

axes[1].plot(vrijeme,brzina)
axes[1].set_title('v-t graf')
axes[1].set_xlabel('t [s]')
axes[1].set_ylabel('v [m/s]')

axes[2].plot(vrijeme,akceleracija)
axes[2].set_title('a-t graf')
axes[2].set_xlabel('t [s]')
axes[2].set_ylabel('a [m/s^2]')

plt.show()