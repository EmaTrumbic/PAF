import matplotlib.pyplot as plt
import numpy as np
import em_field as em

def fE(el):
    xE = el[0]
    yE = el[1]
    zE = el[2]
    return np.array((xE, yE, zE))

def fB(el):
    xB = el[0]
    yB = el[1]
    zB = el[2]*1.002
    return np.array((xB, yB, zB))

p = em.EM_field(np.array((0.,0.,0.)), np.array((0.1,0.1,0.1)), 1., 1., np.array((0.,0.,0.)), fE, np.array((0.,0.,1.)), fB, 0.1)
p.plot_trajectory(10.)
