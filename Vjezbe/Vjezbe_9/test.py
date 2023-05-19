import matplotlib.pyplot as plt
import numpy as np
import gravity as g

#Stvaranje sustava Sunce-Zemlja sa razlicitim dt
p1 = g.Gravity(np.array((0.,0.)),np.array((0.,0.)),1.989*10**30,np.array((1.486*10**11,0.)),np.array((0.,29783.)),5.9742*10**24,3600.) #dt = 1 h
p2 = g.Gravity(np.array((0.,0.)),np.array((0.,0.)),1.989*10**30,np.array((1.486*10**11,0.)),np.array((0.,29783.)),5.9742*10**24,86400.) #dt = 1 dan
p3 = g.Gravity(np.array((0.,0.)),np.array((0.,0.)),1.989*10**30,np.array((1.486*10**11,0.)),np.array((0.,29783.)),5.9742*10**24,2629814.4) #dt = 1 mjesec
p4 = g.Gravity(np.array((0.,0.)),np.array((0.,0.)),1.989*10**30,np.array((1.486*10**11,0.)),np.array((0.,29783.)),5.9742*10**24,7889443.2) #dt = 3 mjeseca

#Plotanje putanje Zemlje oko Sunca (dt = 1h)
p1.plot_trajectory(31556908.8)
plt.title('Putanja Zemlje oko Sunca')
plt.legend(['Sunce', 'Zemlja'])
plt.show()

p2.move(31556908.8)
p3.move(31556908.8)
p4.move(31556908.8)

#Usporedba preciznosti za razne dt
plt.plot(p1.returnInfo()[6], p1.returnInfo()[7], 'orange')
plt.plot(p1.returnInfo()[8], p1.returnInfo()[9])
plt.plot(p2.returnInfo()[8], p2.returnInfo()[9])
plt.plot(p3.returnInfo()[8], p3.returnInfo()[9])
plt.plot(p4.returnInfo()[8], p4.returnInfo()[9])
plt.title('Usporedba preciznosti putanje Zemlje oko Sunca')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend(['', 'dt = 1 h', 'dt = 1 dan', 'dt = 1 mjesec', 'dt = 3 mjeseca'])
plt.show()