import numpy as np
import math
class Particle:
    def __init__(self, x, y, v, kut):
        self.x = x
        self.y = y
        self.v = v
        self.kut = kut
        self.vx = v * math.cos(kut*np.pi/180)
        self.vy = v * math.sin(kut*np.pi/180)
        self.lista_x = [self.x]
        self.lista_y = [self.y]
        self.lista_vy = [self.vy]
    
    def reset(self):
        self.x = 0
        self.y = 0
        self.v = 0
        self.kut = 0
        self.vx = 0
        self.vy = 0
    
    def __move(self, dt):
        g = 9.81
        self.vy -= g*dt
        self.y += self.vy*dt
        self.x += self.vx*dt
        self.lista_vy.append(self.vy)
        self.lista_y.append(self.y)
        self.lista_x.apend(self.x)
        print(self.lista_x, self.lista_y, self.lista_vy)

