import matplotlib.pyplot as plt
import numpy as np
import projectile as p

p1 = p.Projectile(0.,0.,50.,45.,2.,1.22521,0.2,0.02,0.001)
p2 = p.Projectile(0.,0.,50.,45.,2.,1.22521,0.2,0.02,0.01)
p3 = p.Projectile(0.,0.,50.,45.,2.,1.22521,0.,0.02,0.001)

p1.plot_trajectory(False)
p2.plot_trajectory(False)
p2.reset()
p2.plot_trajectory(True)
p3.plot_trajectory(False)
plt.legend(['dt = 0.001', 'dt = 0.01', 'dt = 0.01 (Runge-Kutta)', 'dt = 0.001, Cd = 0'])
plt.show()
