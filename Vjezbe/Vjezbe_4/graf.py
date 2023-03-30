import matplotlib.pyplot as plt
import numpy as np
import particle as pt
p = pt.Particle(0,0,10,60)

vrijeme = np.linspace(0.01, 0.2, 999)
analiticko_rj = 8.828

odstupanje = []
for dt in vrijeme:
    odstupanje.append((abs(analiticko_rj-p.range(dt))/analiticko_rj)*100)
    p.reset()

plt.plot(vrijeme, odstupanje)
plt.title('Ovisnost odstupanja o koraku dt')
plt.xlabel('dt [s]')
plt.ylabel('Odstupanje [%]')
plt.show()