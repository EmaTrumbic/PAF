import harmonic_oscillator as h
import matplotlib.pyplot as plt
import numpy as np

h1 = h.HarmonicOscillator(2,2,3,1,0.01)
h2 = h.HarmonicOscillator(2,2,3,1,0.1)

t1 = np.arange(0, 20, 0.01)
t2 = np.arange(0, 20, 0.1)

for el in range(len(t1)-1):
    h1.move()
for el in range(len(t2)-1):
    h2.move()

plt.plot(h1.plot_analitical()[0], h1.plot_analitical()[1])
plt.plot(t1, h1.returnInfo()[0], 'go', markersize=0.3)
plt.plot(t2, h2.returnInfo()[0], 'ro', markersize=1)
plt.title('Preciznost')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.show()