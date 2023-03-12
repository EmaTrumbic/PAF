import matplotlib.pyplot as plt
import numpy as np

def jednoliko_gibanje(F,m,t):
    a = F/m
    v = 0
    x = 0
    akceleracija = []
    brzina = []
    pomak = []
    proteklo_vrijeme = 0
    vrijeme = []

    while proteklo_vrijeme<t:
        vrijeme.append(proteklo_vrijeme)
        akceleracija.append(a)
        brzina.append(v)
        pomak.append(x)
        v += a*0.01
        x += v*0.01
        proteklo_vrijeme += 0.01
    
    fig, axes = plt.subplots(nrows=1, ncols=3)

    axes[0].plot(vrijeme,pomak)
    axes[0].set_title('x-t graf')
    axes[0].set_xlabel('t [s]')
    axes[0].set_ylabel('x [m]')
    
    axes[1].plot(vrijeme,brzina)
    axes[1].set_title('v-t graf')
    axes[1].set_xlabel('t [s]')
    axes[1].set_ylabel('v [m/s]')
    
    axes[2].plot(vrijeme,akceleracija)
    axes[2].set_title('a-t graf')
    axes[2].set_xlabel('t [s]')
    axes[2].set_ylabel('a [m/s^2]')
    
    plt.show()

def kosi_hitac(v0,θ,t):
    θ *= 3.14159265358979323846264/180

    v0x = v0 * np.cos(θ)
    v0y = v0 * np.sin(θ)
    
    x = 0
    y = 0
    lista_x=[]
    lista_y=[]
    proteklo_vrijeme=0
    vrijeme=[]
    
    while proteklo_vrijeme<t:
        vrijeme.append(proteklo_vrijeme)
        lista_x.append(x)
        lista_y.append(y)
        x += v0x*0.001
        y += v0y*0.001
        v0y -= 9.81*0.001
        proteklo_vrijeme += 0.001
    
    fig, axes = plt.subplots(nrows=1, ncols=3)

    axes[0].plot(lista_x,lista_y)
    axes[0].set_xlabel('x [m]')
    axes[0].set_ylabel('y [m]')
    axes[0].set_title('x-y graf')

    axes[1].plot(vrijeme,lista_x)
    axes[1].set_xlabel('t [s]')
    axes[1].set_ylabel('x [m]')
    axes[1].set_title('x-t graf')

    axes[2].plot(vrijeme,lista_y)
    axes[2].set_xlabel('t [s]')
    axes[2].set_ylabel('y [m]')
    axes[2].set_title('y-t graf')

    plt.show()

