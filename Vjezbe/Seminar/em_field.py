#Napisite program koji crta putanju nabijene cestice u vremenski promjenjivom elektricnom i magnetnom polju
#Demonstrirajte valjanost putanje za slucaj nabijene cestice koja se giba u vremenski promjenjivom
#magnetnom polju B(t) = (0, 0, B(t)) i ima sve tri komponente pocetne brzine razlicite od 0. Neka se magnetno
#polje mijenja linearno i neka u pocetnom trenutku iznosi B(t = 0) = 0, a u konacnom B(t = 10) = 1.
#Usporedite putanju elektrona u konstantnom i vremenski promjenjivom magnetnom polju.
#Usporedite putanje elektrona i pozitrona u vremenski promjenjivom magnetnom polju.

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
class EM_field:
    def __init__(self, r, v, m, q, E, fE, B, fB, dt):
        self.r = [r]
        self.v = [v]
        self.m = m
        self.q = q
        self.E = [E]
        self.fE = fE
        self.B = [B]
        self.fB = fB
        self.a = [self.q/self.m * (self.E[-1] + np.cross(self.v[-1],self.B[-1]))]
        self.dt = dt
        self.x = []
        self.y = []
        self.z = []

    def returnInfo(self):
        return self.r, self.v, self.a, self.E, self.B, self.x, self.y, self.z

    def reset(self):
        self.r = [self.r[0]]
        self.v = [self.v[0]]
        self.a = [self.q/self.m * (self.E[0] + np.cross(self.v[0],self.B[0]))]
        self.E = [self.E[0]]
        self.B = [self.B[0]]

    def move(self, t):
        for i in np.arange(self.dt, t, self.dt):
            self.r.append(self.r[-1] + self.v[-1]*self.dt)
            self.v.append(self.v[-1] + self.a[-1]*self.dt)
            self.E.append(self.fE(self.E[-1]))
            self.B.append(self.fB(self.B[-1]))
            self.a.append(self.q/self.m * (self.E[-1] + np.cross(self.v[-1],self.B[-1])))
        self.x = [el[0] for el in self.r]
        self.y = [el[1] for el in self.r]
        self.z = [el[2] for el in self.r]
    
    def plot_trajectory(self, t):
        EM_field.move(self, t)
        ax = plt.axes(projection='3d')
        ax.plot(self.x,self.y,self.z)
        plt.show()