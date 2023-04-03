import calculus as cal
import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return 5*(x**3)-2*(x**2)+2*x-3

def df1(x):
    return 15*(x**2)-4*x+2

def f2(x):
    return np.sin(x)

print(cal.derivation2(f1, 1, 10, 0.1, False))
print(cal.derivation2(f1, 1, 10, 0.1, True))

plt.plot(cal.derivation2(f1, -2, 2, 0.1,)[0], df1(cal.derivation2(f1, -2, 2, 0.1)[0]))
plt.plot(cal.derivation2(f1, -2, 2, 0.1)[0], cal.derivation2(f1, -2, 2, 0.1)[1], 'ro')
plt.plot(cal.derivation2(f1, -2, 2, 0.01)[0], cal.derivation2(f1, -2, 2, 0.01)[1], 'go')
plt.show()