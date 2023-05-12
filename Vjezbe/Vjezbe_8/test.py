import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import em_polje as em

#Stvaranje cestica (3 pozitrona sa razlicitm dt, 1 elektron)
p = em.Particle(np.array((0,0,0)),1,1,np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),0.01)
p1 = em.Particle(np.array((0,0,0)),1,1,np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),0.1)
p2 = em.Particle(np.array((0,0,0)),1,1,np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),0.15)
e = em.Particle(np.array((0,0,0)),1,-1,np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),0.01)

#Zasebni grafovi za jednu cesticu
p.plot_trajectory(20)
plt.title('Pozitron')
plt.show()
e.plot_trajectory(20)
plt.title('Elektron')
plt.show()

#Usporedba putanja pozitrona i elektrona
ax = plt.axes(projection='3d')
ax.plot3D(p.returnInfo()[3],p.returnInfo()[4],p.returnInfo()[5])
ax.plot3D(e.returnInfo()[3],e.returnInfo()[4],e.returnInfo()[5])
ax.set_title('Pozitron i elektron')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.legend(['Pozitron', 'Elektron'])
plt.show()

#Usporedba preciznosti
p1.move(20)
p2.move(20)
ax = plt.axes(projection='3d')
ax.plot3D(p.returnInfo()[3],p.returnInfo()[4],p.returnInfo()[5])
ax.plot3D(p1.returnInfo()[3],p1.returnInfo()[4],p1.returnInfo()[5])
ax.plot3D(p2.returnInfo()[3],p2.returnInfo()[4],p2.returnInfo()[5])
ax.set_title('Preciznost za pozitron (Euler)')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.legend(['dt = 0.01 s', 'dt = 0.1 s', 'dt = 0.15 s'])
plt.show()