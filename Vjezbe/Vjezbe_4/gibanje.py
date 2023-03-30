import particle as pt
p = pt.Particle(20,80,70,60)
print('Domet = {} m'.format(p.range(0.01)))
p.plot_trajectory(0.01)

analiticko_rj = 494.6
print('Odstupanje = {}%'.format((abs(analiticko_rj-p.range(0.01))/analiticko_rj)*100))