import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from numpy import linalg as LA
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

    def moveEuler(self, t):
        for i in np.arange(self.dt, t, self.dt):
            self.r.append(self.r[-1] + self.v[-1]*self.dt)
            self.v.append(self.v[-1] + self.a[-1]*self.dt)
            self.E.append(self.fE(self.E[-1]))
            self.B.append(self.fB(self.B[-1]))
            self.a.append(self.q/self.m * (self.E[-1] + np.cross(self.v[-1],self.B[-1])))
        self.x = [el[0] for el in self.r]
        self.y = [el[1] for el in self.r]
        self.z = [el[2] for el in self.r]
    
    def moveRungeKutta(self, t):
        for i in np.arange(self.dt, t, self.dt):
            k_v = [self.q/self.m * (self.E[-1] + np.cross(self.v[-1],self.B[-1]))*self.dt]
            k_r = [self.v[-1]*self.dt]
            for j in range(3):
                k_v.append(self.q/self.m * (self.E[-1] + np.cross((self.v[-1]+0.5*k_v[-1]),self.B[-1]))*self.dt)
                k_r.append((self.v[-1]+0.5*k_v[-1])*self.dt)
            self.v.append(self.v[-1]+(k_v[0]+2*k_v[1]+2*k_v[2]+k_v[3])/6)
            self.r.append(self.r[-1]+(k_r[0]+2*k_r[1]+2*k_r[2]+k_r[3])/6)
            self.E.append(self.fE(self.E[-1]))
            self.B.append(self.fB(self.B[-1]))
            self.a.append(self.q/self.m * (self.E[-1] + np.cross(self.v[-1],self.B[-1])))
        self.x = [el[0] for el in self.r]
        self.y = [el[1] for el in self.r]
        self.z = [el[2] for el in self.r]
    
    def plot_trajectory(self, t, title, useRungeKutta = True):
        if useRungeKutta == True:
            EM_field.moveRungeKutta(self, t)
        else:
            EM_field.moveEuler(self, t)
        ax = plt.axes(projection='3d')
        ax.plot(self.x,self.y,self.z)
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')
        ax.set_zlabel('z [m]')
        ax.set_title(title)
        plt.show()
