import matplotlib.pyplot as plt
import numpy as np
#gustoca zraka: 1,22521 kg/m^3
class Projectile:
    def __init__(self, x, y, v, kut, m, p, Cd, A, dt):
        self.x = x
        self.y = y
        self.v = v
        self.kut = kut*np.pi/180
        self.m = m
        self.p = p
        self.Cd = Cd
        self.A = A
        self.dt = dt
        self.lista_x = [self.x]
        self.lista_y = [self.y]
        self.lista_vx = [self.v * np.cos(self.kut)]
        self.lista_vy = [self.v * np.sin(self.kut)]
        self.lista_ax = [(-1*self.lista_vx[-1]/abs(self.lista_vx[-1]))*(self.p*self.Cd*self.A/(2*self.m))*(self.lista_vx[-1])**2]
        self.lista_ay = [(-1*self.lista_vy[-1]/abs(self.lista_vy[-1]))*(self.p*self.Cd*self.A/(2*self.m))*(self.lista_vx[-1])**2]
    
    def returnInfo(self):
        return self.lista_x, self.lista_y, self.lista_vx, self.lista_vy, self.lista_ax, self.lista_ay
    
    def __move(self):
        while self.lista_y[-1]>=0:
            self.lista_x.append(self.lista_x[-1]+(self.lista_vx[-1]*self.dt))
            self.lista_y.append(self.lista_y[-1]+(self.lista_vy[-1]*self.dt))
            self.lista_vx.append(self.lista_vx[-1]+(self.lista_ax[-1]*self.dt))
            self.lista_vy.append(self.lista_vy[-1]+(self.lista_ay[-1]*self.dt))
            self.lista_ax.append((-1*self.lista_vx[-1]/abs(self.lista_vx[-1]))*(self.p*self.Cd*self.A/(2*self.m))*(self.lista_vx[-1])**2)
            self.lista_ay.append(-9.81-(self.lista_vy[-1]/abs(self.lista_vy[-1]))*(self.p*self.Cd*self.A/(2*self.m))*(self.lista_vy[-1])**2)
    
    def plot_trajectory(self, showPlot = True):
        Projectile.__move(self)
        plt.plot(self.lista_x, self.lista_y)
        plt.title('x-y graf')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        if showPlot == True:
            plt.show()