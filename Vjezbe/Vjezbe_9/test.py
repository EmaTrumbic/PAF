import numpy as np
import gravity as g
#p = g.Gravity(np.array((0,0)),np.array((0,10)),1500000000,np.array((2,1)),np.array((4,2)),20000000000000,0.01)
#p.plot_trajectory(300)

p = g.Gravity(np.array((0,0)),np.array((0,0)),1.989*10**30,np.array((1.486*10**11,0)),np.array((0,29783)),5.9742*10**24,3600)
p.plot_trajectory(31556908800)
