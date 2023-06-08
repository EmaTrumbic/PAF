import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
import em_field as em

def f_constant(el):
    return el

def f(el):
    return np.array((el[0], el[1], el[2]+0.001))


e1 = em.EM_field(np.array((0.,0.,0.)), np.array((0.1,0.1,0.1)), 1., -1., np.array((0.,0.,0.)), f_constant, np.array((0.,0.,1.)), f_constant, 0.01)
e2 = em.EM_field(np.array((0.,0.,0.)), np.array((0.1,0.1,0.1)), 1., -1., np.array((0.,0.,0.)), f_constant, np.array((0.,0.,0.)), f, 0.01)
p1 = em.EM_field(np.array((0.,0.,0.)), np.array((0.1,0.1,0.1)), 1., 1., np.array((0.,0.,0.)), f_constant, np.array((0.,0.,0.)), f, 0.01)
p2 = em.EM_field(np.array((0.,0.,0.)), np.array((0.1,0.1,0.1)), 1., 1., np.array((0.,0.,1.)), f_constant, np.array((0.,0.,0.)), f_constant, 0.01)
p3 = em.EM_field(np.array((0.,0.,0.)), np.array((0.1,0.1,0.1)), 1., 1., np.array((0.,0.,0.)), f, np.array((0.,0.,0.)), f_constant, 0.01)

#Ucinci elektromagnetskog polja bolje se uocavaju na vremenskom intervalu od 20 sekundi umjesto 10 (kao sto se vidi na iduca 2 grafa)
#Zbog toga su svi grafovi napravljeni tako da se cestice krecu 20 sekundi
e2.plot_trajectory(10., 'Putanja elektrona u rastucem polju 10 sekundi')
e2.reset()
e2.plot_trajectory(20., 'Putanja elektrona u rastucem polju 20 sekundi')

#Potrebno je pomaknuti cestice cije informacije zelimo plottati ako za plottanje koristimo returnInfo() umjesto plot_trajectory()
#Jer plot_trajectory sam pomakne cestice
e1.moveRungeKutta(20.)
p1.moveRungeKutta(20.)

ax = plt.axes(projection='3d')
ax.plot(e1.returnInfo()[5],e1.returnInfo()[6],e1.returnInfo()[7])
ax.plot(e2.returnInfo()[5],e2.returnInfo()[6],e2.returnInfo()[7])
ax.set_title('Usporedba putanje elektrona u konst. i rastucem B polju')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.legend(['Konstantno polje', 'Rastuce polje'])
plt.show()

ax = plt.axes(projection='3d')
ax.plot(p1.returnInfo()[5],p1.returnInfo()[6],p1.returnInfo()[7])
ax.plot(e2.returnInfo()[5],e2.returnInfo()[6],e2.returnInfo()[7])
ax.set_title('Usporedba putanje pozitrona i elektrona u rastucem B polju')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.legend(['Pozitron', 'Elektron'])
plt.show()

ax = plt.axes(projection='3d')
ax.plot(p1.returnInfo()[5],p1.returnInfo()[6],p1.returnInfo()[7])
p1.reset()
p1.moveEuler(20.)
ax.plot(p1.returnInfo()[5],p1.returnInfo()[6],p1.returnInfo()[7])
ax.set_title('Usporedba putanje pozitrona u rastucem B polju')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.legend(['Runge-Kutta', 'Euler'])
plt.show()

listEuler = [el for el in p1.returnInfo()[0]]
p1.reset()
p1.moveRungeKutta(20.)
comparison_list = [LA.norm(p1.returnInfo()[0][i]-listEuler[i]) for i in range(len(listEuler)) if i%10 == 0] #Plottanje svako desete tocke da ih ne bude previse
plt.plot(np.arange(0., 20., 0.1), comparison_list, 'o', markersize=1)
plt.xlabel('Vrijeme [s]')
plt.ylabel('Razlika [m]')
plt.title('Razlika izmedu Euler i Runge-Kutta metode')
plt.show()

p2.plot_trajectory(20., 'Pozitron u konst. E polju')
plt.plot(np.arange(0., 20., 0.01), [el[0] for el in p2.returnInfo()[1]]) #p2.returnInfo()[1] je lista vektora brzina, plottamo svaku komponentu posebno
plt.plot(np.arange(0., 20., 0.01), [el[1] for el in p2.returnInfo()[1]])
plt.plot(np.arange(0., 20., 0.01), [el[2] for el in p2.returnInfo()[1]])
plt.xlabel('Vrijeme [s]')
plt.ylabel('Brzina [m/s]')
plt.legend(['x komponenta', 'y komponenta', 'z komponenta'])
plt.title('Brzina pozitrona u konst. E polju')
plt.show()

p3.plot_trajectory(20., 'Pozitron u rastucem E polju')
plt.plot(np.arange(0., 20., 0.01), [el[0] for el in p3.returnInfo()[1]])
plt.plot(np.arange(0., 20., 0.01), [el[1] for el in p3.returnInfo()[1]])
plt.plot(np.arange(0., 20., 0.01), [el[2] for el in p3.returnInfo()[1]])
plt.xlabel('Vrijeme [s]')
plt.ylabel('Brzina [m/s]')
plt.legend(['x komponenta', 'y komponenta', 'z komponenta'])
plt.title('Brzina pozitrona u rastucem E polju')
plt.show()

plt.plot(np.arange(0., 20., 0.01), [el[0] for el in p1.returnInfo()[1]])
plt.plot(np.arange(0., 20., 0.01), [el[1] for el in p1.returnInfo()[1]])
plt.plot(np.arange(0., 20., 0.01), [el[2] for el in p1.returnInfo()[1]])
plt.xlabel('Vrijeme [s]')
plt.ylabel('Brzina [m/s]')
plt.legend(['x komponenta', 'y komponenta', 'z komponenta'])
plt.title('Brzina pozitrona u rastucem B polju')
plt.show()

#Racunanje vremenskog intervala potrebnog za jedan puni krug
#Formula je T=2*pi*m/qB
#Uzimamo normalu od vektora magnetskog polja jer nam je bitan samo iznos, a ne zelimo da nam vrijeme bude vektor
#Range krece od 1 jer je u pocetnom trenutku B=0, pa ne zelimo dijeliti s nulom
T = [2.*np.pi*p1.returnInfo()[8]/(p1.returnInfo()[9]*LA.norm(p1.returnInfo()[4][i])) for i in range(1, len(p1.returnInfo()[4]))]
plt.plot(np.arange(0.01, 20., 0.01), T, 'o', markersize=1)
plt.title('Mjenjanje perioda kruzenja u promjenjivom B polju')
plt.xlabel('Vrijeme [s]')
plt.ylabel('Period kruzenja [s]')
plt.show()