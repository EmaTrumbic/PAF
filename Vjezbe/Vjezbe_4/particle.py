import matplotlib.pyplot as plt
import numpy as np
class Particle:
    def __init__(self, x, y, v, kut):
        self.x = x
        self.y = y
        self.v = v
        self.kut = kut
        self.lista_x = [x]
        self.lista_y = [y]
        self.vx = v * np.cos(kut*np.pi/180)
        self.lista_vy = [v * np.sin(kut*np.pi/180)]
    
    def reset(self):
        self.lista_x = [self.x]
        self.lista_y = [self.y]
        self.lista_vy = [self.v * np.sin(self.kut*np.pi/180)]
    
    def __move(self, dt):
        g = 9.81
        self.lista_x.append(self.lista_x[-1]+(dt*self.vx))
        self.lista_y.append(self.lista_y[-1]+(dt*self.lista_vy[-1]))
        self.lista_vy.append(self.lista_vy[-1]-(g*dt))
    
    def range(self, dt):
        while self.lista_y[-1] >= 0:
            Particle.__move(self,dt)
        return self.lista_x[-1]
    
    def plot_trajectory(self, dt):
        while self.lista_y[-1] >= 0:
            Particle.__move(self,dt)
        plt.plot(self.lista_x, self.lista_y)
        plt.title('x-y graf')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.show()
