import matplotlib.pyplot as plt
import numpy as np
import em_field as em

#Funkcija za konstantno elektricno polje
def fE(el):
    return el

#Funkcija za konstantno magnetno polje
def fB1(el):
    return el

#Funkcija za promjenjivo magnetno polje
def fB2(el):
    return np.array((el[0], el[1], el[2]+0.001))

#Elektron u konstatnom polju
e1 = em.EM_field(np.array((0.,0.,0.)), np.array((0.1,0.1,0.1)), 1., -1., np.array((0.,0.,0.)), fE, np.array((0.,0.,1.)), fB1, 0.01)

#Elektron u promjenjivom polju
e2 = em.EM_field(np.array((0.,0.,0.)), np.array((0.1,0.1,0.1)), 1., -1., np.array((0.,0.,0.)), fE, np.array((0.,0.,0.)), fB2, 0.01)

#Pozitron u promjenjivom polju
p = em.EM_field(np.array((0.,0.,0.)), np.array((0.1,0.1,0.1)), 1., 1., np.array((0.,0.,0.)), fE, np.array((0.,0.,0.)), fB2, 0.01)

e1.moveEuler(20.)
e2.moveEuler(20.)
p.moveEuler(20.)

ax = plt.axes(projection='3d')
ax.plot(e1.returnInfo()[5],e1.returnInfo()[6],e1.returnInfo()[7])
ax.plot(e2.returnInfo()[5],e2.returnInfo()[6],e2.returnInfo()[7])
ax.set_title('Usporedba putanje elektrona u konstatnom i promjenjivom polju')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.legend(['Konstantno polje', 'Promjenjivo polje'])
plt.show()

ax = plt.axes(projection='3d')
ax.plot(p.returnInfo()[5],p.returnInfo()[6],p.returnInfo()[7])
ax.plot(e2.returnInfo()[5],e2.returnInfo()[6],e2.returnInfo()[7])
ax.set_title('Usporedba putanje pozitrona i elektrona u promjenjivom polju')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.legend(['Pozitron', 'Elektron'])
plt.show()

ax = plt.axes(projection='3d')
ax.plot(p.returnInfo()[5],p.returnInfo()[6],p.returnInfo()[7])
p.reset()
p.moveRungeKutta(20.)
ax.plot(p.returnInfo()[5],p.returnInfo()[6],p.returnInfo()[7])
ax.set_title('Usporedba putanje pozitrona u promjenjivom polju')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.legend(['Euler', 'Runge-Kutta'])
plt.show()

plt.plot(np.arange(0., 20., 0.01), p.compare(20.))
plt.xlabel('Vrijeme')
plt.ylabel('Razlika')
plt.title('Razlika izmedu Euler i Runge-Kutta metode')
plt.show()