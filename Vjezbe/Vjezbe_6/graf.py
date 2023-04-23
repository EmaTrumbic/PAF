import harmonic_oscillator as h
import matplotlib.pyplot as plt
import numpy as np

h1 = h.HarmonicOscillator(3,2,3,1,0.01)
h2 = h.HarmonicOscillator(3,2,3,1,0.1)
h3 = h.HarmonicOscillator(3,2,3,1,0.2)
h4 = h.HarmonicOscillator(3,2,3,1,0.5)

h1.plot_trajectory(20)
h2.move(20)
h3.move(20)
h4.move(20)

h1.plot_analitical()
plt.plot(h1.returnInfo()[3], h1.returnInfo()[0], 'go', markersize=0.3)
plt.plot(h2.returnInfo()[3], h2.returnInfo()[0], 'ro', markersize=1)
plt.title('Preciznost')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.show()

analiticki_period = 2*np.pi*np.sqrt(h1.returnInfo()[-1]/h1.returnInfo()[-2])
print('Analiticki period: {}'.format(analiticki_period))

plt.plot([0.01, 0.1, 0.2, 0.5], [analiticki_period, analiticki_period, analiticki_period, analiticki_period])
plt.plot([0.01, 0.1, 0.2, 0.5], [h1.numericalPeriod(), h2.numericalPeriod(), h3.numericalPeriod(), h4.numericalPeriod()], 'o')
plt.xlabel('Korak')
plt.ylabel('Numericki period')
plt.title('Preciznost numerickog perioda')
plt.show()
