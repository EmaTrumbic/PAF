import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import em_polje as em

p = em.Particle(np.array((0,0,0)),1,1,np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),0.01)
e = em.Particle(np.array((0,0,0)),1,-1,np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),0.01)

p.plot_trajectory(20)
plt.title('Pozitron')
plt.show()
e.plot_trajectory(20)
plt.title('Elektron')
plt.show()