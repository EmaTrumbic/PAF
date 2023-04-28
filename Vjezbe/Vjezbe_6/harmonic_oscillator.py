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
    
    def returnInfo(self):
        return self.lista_x, self.lista_v, self.lista_a, self.lista_t, self.k, self.m
    
    def move(self, t):
        for i in np.arange(self.dt, t, self.dt):
            self.lista_x.append(self.lista_x[-1]+(self.lista_v[-1]*self.dt))
            self.lista_v.append(self.lista_v[-1]+(self.lista_a[-1]*self.dt))
            self.lista_a.append(-1*self.k*self.lista_x[-1]/self.m)
            self.lista_t.append(self.lista_t[-1]+self.dt)
    
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

    def plot_analitical(self, t, showPlot = True):
        A = np.sqrt((self.x)**2+((self.m/self.k)*(self.v)**2))
        fi = np.arcsin(self.x/A)
        vrijeme = np.arange(0, t, self.dt)
        lista = []
        for t in vrijeme:
            lista.append(A * np.sin(np.sqrt(self.k/self.m) * t + fi))
        plt.plot(vrijeme, lista)
        if showPlot == True:
            plt.show()

    #Numericki period racunam tako da za pocetni trenutak uzmem trenutak kada je tijelo preslo ravnotezni polozaj po prvi put, tj onda su trenutni x i pocetni x suprotnih predznaka, pa je njihov omjer negativan
    #Zatim za konacan trenutak uzmem trenutak kad je tijelo opet preslo ravnotezni polozaj i vratilo se na pocetnu stranu, pa su trenutni x i pocetni x istog predznaka
    #Taj vremeneski interval je zapravo pola perioda, pa ga pomnozim sa 2 da dobijem period
    def numericalPeriod(self):
        HarmonicOscillator.reset(self)
        HarmonicOscillator.move(self, 4*np.pi*np.sqrt(HarmonicOscillator.returnInfo(self)[-1]/HarmonicOscillator.returnInfo(self)[-2]))
        z = False
        for i in range(len(self.lista_x)):
            if z == False:
                if self.lista_x[0]/self.lista_x[i] < 0:
                    z = True
                    t0 = self.lista_t[i]
            if z == True:
                if self.lista_x[0]/self.lista_x[i] > 0:
                    t1 = self.lista_t[i]
                    break
        return 2.*(t1-t0)