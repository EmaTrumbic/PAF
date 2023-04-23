import matplotlib.pyplot as plt
import numpy as np
class HarmonicOscillator:
    def __init__(self, x, v, m, k, dt):
        self.x = x
        self.v = v
        self.k = k
        self.m = m
        self.dt = dt
        self.lista_x = [x]
        self.lista_v = [v]
        self.lista_a = [-1*self.k*self.x/self.m]
        self.lista_t = [0]
    
    def reset(self):
        self.lista_x = [self.x]
        self.lista_v = [self.v]
        self.lista_a = [-1*self.k*self.x/self.m]
        self.lista_t = [0]
    
    def move(self, t):
        for i in np.arange(self.dt, t, self.dt):
            self.lista_x.append(self.lista_x[-1]+(self.lista_v[-1]*self.dt))
            self.lista_v.append(self.lista_v[-1]+(self.lista_a[-1]*self.dt))
            self.lista_a.append(-1*self.k*self.lista_x[-1]/self.m)
            self.lista_t.append(self.lista_t[-1]+self.dt)
    
    def returnInfo(self):
        return self.lista_x, self.lista_v, self.lista_a, self.lista_t, self.k, self.m
    
    def plot_trajectory(self, t):
        HarmonicOscillator.move(self, t)
        
        fig, axes = plt.subplots(nrows=3, ncols=1)

        axes[0].plot(self.lista_t, self.lista_x)
        axes[0].set_title('x-t graf')
        axes[0].set_xlabel('t [s]')
        axes[0].set_ylabel('x [m]')

        axes[1].plot(self.lista_t, self.lista_v)
        axes[1].set_title('v-t graf')
        axes[1].set_xlabel('t [s]')
        axes[1].set_ylabel('v [m/s]')

        axes[2].plot(self.lista_t, self.lista_a)
        axes[2].set_title('a-t graf')
        axes[2].set_xlabel('t [s]')
        axes[2].set_ylabel('a [m/s^2]')

        plt.show()
    
    def numericalPeriod(self):
        HarmonicOscillator.reset(self)
        HarmonicOscillator.move(self, 4*np.pi*np.sqrt(HarmonicOscillator.returnInfo(self)[-1]/HarmonicOscillator.returnInfo(self)[-2]))
        x = -1
        for i in range(len(self.lista_x)):
            if x == -1:
                if self.lista_x[0]/self.lista_x[i] < 0:
                    x = 0
                    t0 = self.lista_t[i]
            if x == 0:
                if self.lista_x[0]/self.lista_x[i] > 0:
                    t1 = self.lista_t[i]
                    break
        return 2*(t1-t0)
        
    def plot_analitical(self):
        A = np.sqrt((self.x)**2+((self.m/self.k)*(self.v)**2))
        fi = np.arcsin(self.x/A)
        vrijeme = np.arange(0, 20, 0.1)
        lista = []
        for t in vrijeme:
            lista.append(A * np.sin(np.sqrt(self.k/self.m) * t + fi))
        plt.plot(vrijeme, lista)
