import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
class Particle:
    def __init__(self, r, m, q, E, B, v, dt):
        self.r = [r]
        self.m = m
        self.q = q
        self.E = E
        self.B = B
        self.v = [v]
        self.a = [self.q/self.m * (self.E + np.cross(self.v[-1],self.B))]
        self.dt = dt
    
    def reset(self):
        self.r = [self.r[0]]
        self.v = [self.v[0]]
        self.a = [self.q/self.m * (self.E + np.cross(self.v[0],self.B))]

    def returnInfo(self):
        return self.r, self.v, self.a

    def move(self,t):
        for i in np.arange(self.dt, t, self.dt):
            self.r.append(self.r[-1] + self.v[-1]*self.dt)
            self.v.append(self.v[-1] + self.a[-1]*self.dt)
            self.a.append(self.q/self.m * (self.E + np.cross(self.v[-1],self.B)))
    
    def evolve(self,t):
        Particle.move(self,t)
        return self.r
    
    def plot_trajectory(self,t):
        Particle.move(self, t)
        x = []
        y = []
        z = []
        for i in range(len(self.r)):
            x.append(self.r[i][0])
            y.append(self.r[i][1])
            z.append(self.r[i][2])
        ax = plt.axes(projection='3d')
        ax.plot(x,y,z)
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')
        ax.set_zlabel('z [m]')
