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

x1 = []
y1 = []
z1 = []
x2 = []
y2 = []
z2 = []
for i in range(len(p.returnInfo()[0])):
    x1.append(p.returnInfo()[0][i][0])
    y1.append(p.returnInfo()[0][i][1])
    z1.append(p.returnInfo()[0][i][2])
for i in range(len(e.returnInfo()[0])):
    x2.append(e.returnInfo()[0][i][0])
    y2.append(e.returnInfo()[0][i][1])
    z2.append(e.returnInfo()[0][i][2])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x1,y1,z1)
ax.plot3D(x2,y2,z2)
ax.set_title('Pozitron i elektron')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.legend(['Pozitron', 'Elektron'])
plt.show()