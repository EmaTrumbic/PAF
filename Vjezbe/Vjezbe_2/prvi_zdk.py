import matplotlib.pyplot as plt
import numpy as np

F = float(input('Unesite iznos sile (N): '))
m = float(input('Unesite masu (kg): '))

a = F/m
v = 0
x = 0
dt = 0.01
akceleracija = [a]
brzina = [0]
pomak = [0]
t = np.linspace(0,10,1000)

for i in range(999):
    v += a*dt
    x += v*dt
    akceleracija.append(a)
    brzina.append(v)
    pomak.append(x)
    
fig, axes = plt.subplots(nrows=1, ncols=3)

axes[0].plot(t,pomak)
axes[0].set_title('x-t graf')
axes[0].set_xlabel('t [s]')
axes[0].set_ylabel('x [m]')
    
axes[1].plot(t,brzina)
axes[1].set_title('v-t graf')
axes[1].set_xlabel('t [s]')
axes[1].set_ylabel('v [m/s]')
    
axes[2].plot(t,akceleracija)
axes[2].set_title('a-t graf')
axes[2].set_xlabel('t [s]')
axes[2].set_ylabel('a [m/s^2]')
    
plt.show()