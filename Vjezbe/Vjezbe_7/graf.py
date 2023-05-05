import matplotlib.pyplot as plt
import numpy as np
import projectile as p

p1 = p.Projectile(0.,0.,50.,45.,2.,1.22521,0.2,0.02,0.001)
p2 = p.Projectile(0.,0.,50.,45.,2.,1.22521,0.2,0.02,0.01)
p3 = p.Projectile(0.,0.,50.,45.,2.,1.22521,0.2,0.02,0.2)
p4 = p.Projectile(0.,0.,50.,45.,2.,1.22521,0.,0.02,0.001)

p1.plot_trajectory(False)
p2.plot_trajectory(False)
p2.reset()
p2.plot_trajectory()
p3.plot_trajectory(False)
p3.reset()
p3.plot_trajectory()
p4.plot_trajectory(False)
p4.reset()
p4.plot_trajectory()
plt.legend(['dt = 0.001 s', 'dt = 0.01 s', 'dt = 0.01 s (RK)', 'dt = 0.2 s', 'dt = 0.2 s (RK)', 'dt = 0.001 s, Cd = 0', 'dt = 0.001 s, Cd = 0 (RK)'])
plt.show()

#Runge-Kutta metoda je preciznija od Euler-ove za isti korak, a naznake nefizikalnog gibanja se pojavljuju za dt = 0.2 s.
#Za slucaj kada nemamo trenja, Euler-ovom metodom dobijemo malo veci domet i visinu u odnosu na Runge-Kutta metodu.