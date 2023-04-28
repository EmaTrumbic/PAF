import harmonic_oscillator as h
import matplotlib.pyplot as plt
import numpy as np

h0= h.HarmonicOscillator(3.,2.,3.,1.,0.001)
h1 = h.HarmonicOscillator(3.,2.,3.,1.,0.01)
h2 = h.HarmonicOscillator(3.,2.,3.,1.,0.06)
h3 = h.HarmonicOscillator(3.,2.,3.,1.,0.11)
h4 = h.HarmonicOscillator(3.,2.,3.,1.,0.16)
h5 = h.HarmonicOscillator(3.,2.,3.,1.,0.21)
h6 = h.HarmonicOscillator(3.,2.,3.,1.,0.26)
h7 = h.HarmonicOscillator(3.,2.,3.,1.,0.31)
h8 = h.HarmonicOscillator(3.,2.,3.,1.,0.36)
h9 = h.HarmonicOscillator(3.,2.,3.,1.,0.41)
h10 = h.HarmonicOscillator(3.,2.,3.,1.,0.46)
h11 = h.HarmonicOscillator(3.,2.,3.,1.,0.51)

h1.plot_trajectory(20.)
h0.move(20.)
h2.move(20.)
h4.move(20.)

h1.plot_analitical(20, False)
plt.plot(h0.returnInfo()[3], h0.returnInfo()[0], 'o', markersize=0.1)
plt.plot(h1.returnInfo()[3], h1.returnInfo()[0], 'o', markersize=0.3)
plt.plot(h4.returnInfo()[3], h4.returnInfo()[0], 'o', markersize=1)
plt.title('Preciznost')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.legend(['Analiticko', 'dt = 0.001', 'dt = 0.01', 'dt = 0.16'])
plt.show()
#Za male dt-ove graf se samo malo pomakne u stranu, a za vece dolazi do vecih oscilacija, najvise kad je pomak priblizno jednak amplitudi, a kod ravnoteznog polozaja oscilacije su manje

analiticki_period = 2.*np.pi*np.sqrt(h1.returnInfo()[-1]/h1.returnInfo()[-2])
print('Analiticki period: {}'.format(analiticki_period))

plt.axhline(analiticki_period)
plt.plot(np.linspace(0.01, 0.51, 11), [h1.numericalPeriod(), h2.numericalPeriod(), h3.numericalPeriod(), h4.numericalPeriod(), h5.numericalPeriod(), h6.numericalPeriod(), h7.numericalPeriod(), h8.numericalPeriod(), h9.numericalPeriod(), h10.numericalPeriod(), h11.numericalPeriod()], 'ro')
plt.xlabel('Korak')
plt.ylabel('Numericki period')
plt.title('Preciznost numerickog perioda')
plt.legend(['Analiticki period', 'Numericki periodi'])
plt.show()
#Sto je veci dt, to su vece oscilacije, posebno ako period nije djeljiv s dt-om, pa se ne uzme tocno vrijeme kad tijelo prede ravnotezni polozaj, nego je greska veca