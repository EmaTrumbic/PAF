import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
class Gravity:
    def __init__(self,r1,v1,m1,r2,v2,m2,dt):
        self.G = 6.67408*10**(-11)
        self.r1 = [r1]
        self.v1 = [v1]
        self.a1 = []
        self.m1 = m1
        self.r2 = [r2]
        self.v2 = [v2]
        self.a2 = []
        self.m2 = m2
        self.dt = dt
        self.x1 = []
        self.y1 = []
        self.x2 = []
        self.y2 = []
    
    def reset(self):
        self.r1 = [self.r1[0]]
        self.v1 = [self.v1[0]]
        self.a1 = []
        self.r2 = [self.r2[0]]
        self.v2 = [self.v2[0]]
        self.a2 = []
    
    def returnInfo(self):
        return self.r1, self.v1, self.a1, self.r2, self.v2, self.a2
    
    def move(self,t):
        for i in np.arange(self.dt, t, self.dt):
            self.a1.append(-1*self.G*self.m2*(self.r1[-1]-self.r2[-1])/(LA.norm(self.r1[-1]-self.r2[-1]))**3)
            self.v1.append(self.v1[-1] + self.a1[-1]*self.dt)
            self.r1.append(self.r1[-1] + self.v1[-1]*self.dt)
            self.a2.append(-1*self.G*self.m1*(self.r2[-1]-self.r1[-2])/(LA.norm(self.r2[-1]-self.r1[-2]))**3)
            self.v2.append(self.v2[-1] + self.a2[-1]*self.dt)
            self.r2.append(self.r2[-1] + self.v2[-1]*self.dt)
    
    def plot_trajectory(self,t):
        Gravity.move(self,t)
        for i in range(len(self.r1)):
            self.x1.append(self.r1[i][0])
            self.y1.append(self.r1[i][1])
            self.x2.append(self.r2[i][0])
            self.y2.append(self.r2[i][1])
        plt.plot(self.x1, self.y1, 'orange')
        plt.plot(self.x2, self.y2, 'b')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')