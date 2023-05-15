import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
class Gravity:
    def __init__(self,r1,v1,m1,r2,v2,m2,dt):
        self.G = 6.67 * 10**(-11)
        self.d12 = LA.norm(r1[0]-r2[0])
        self.d21 = LA.norm(r2[0]-r1[0])
        self.r1 = [r1]
        self.v1 = [v1]
        self.a1 = [-1*self.G*m2*self.d12/self.d12**3]
        self.m1 = m1
        self.r2 = [r2]
        self.v2 = [v2]
        self.a2 = [-1*self.G*m1*self.d21/self.d21**3]
        self.m2 = m2
        self.dt = dt
        self.x1 = []
        self.y1 = []
        self.x2 = []
        self.y2 = []
    
    def reset(self):
        self.r1 = [self.r1[0]]
        self.v1 = [self.v1[0]]
        self.a1 = [-1*self.G*self.m2*(self.r1[0]-self.r2[0])/np.dot((self.r1[0]-self.r2[0]),(self.r1[0]-self.r2[0]),(self.r1[0]-self.r2[0]))]
        self.r2 = [self.r2[0]]
        self.v2 = [self.v2[0]]
        self.a2 = [-1*self.G*self.m1*(self.r2[0]-self.r1[0])/np.dot((self.r2[0]-self.r1[0]),(self.r2[0]-self.r1[0]),(self.r2[0]-self.r1[0]))]
    
    def returnInfo(self):
        return self.r1, self.v1, self.a1, self.r2, self.v2, self.a2,
    
    def move(self,t):
        for i in (self.dt, t, self.dt):
            print((self.r1[-1]-self.r2[-1])**3)
            self.a1.append(-1*self.G*self.m2*(self.r1[-1]-self.r2[-1])/np.dot((self.r1[-1]-self.r2[-1]),(self.r1[-1]-self.r2[-1]),(self.r1[-1]-self.r2[-1])))
            self.v1.append(self.v1[-1] + self.a1[-1]*self.dt)
            self.r1.append(self.r1[-1] + self.v1[-1]*self.dt)
            self.a2.append(-1*self.G*self.m1*(self.r2[-1]-self.r1[-1])/np.dot((self.r2[-1]-self.r1[-1]),(self.r2[-1]-self.r1[-1]),(self.r2[-1]-self.r1[-1])))
            self.v2.append(self.v2[-1] + self.a2[-1]*self.dt)
            self.r2.append(self.r2[-1] + self.v2[-1]*self.dt)
    
    def plot_trajectory(self,t):
        Gravity.move(self,t)
        for i in range(len(self.r1)):
            self.x1.append(self.r1[i][0])
            self.y1.append(self.r1[i][1])
            self.x2.append(self.r2[i][0])
            self.y2.append(self.r2[i][1])
        plt.plot(self.x1, self.y1)
        plt.plot(self.x2, self.y2)
        plt.show()
