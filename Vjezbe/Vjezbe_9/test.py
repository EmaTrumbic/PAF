import matplotlib.pyplot as plt
import numpy as np
import gravity as g

p = g.Gravity(np.array((0,0)),np.array((0,0)),1.989*10**30,np.array((1.486*10**11,0)),np.array((0,29783)),5.9742*10**24,86400)
p.plot_trajectory(31556908.8)
plt.legend(['Sunce', 'Zemlja'])
plt.show()
