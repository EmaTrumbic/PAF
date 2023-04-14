import calculus as cal; import matplotlib.pyplot as plt; import numpy as np

def f1(x):
    return 5*(x**3)-2*(x**2)+2*x-3
def df1(x):
    return 15*(x**2)-4*x+2
def f2(x):
    return np.sin(x)
def f3(x):
    return 2*(x**2)+3
def f4(x):
    return -x**2+5


print('Derivacija kubne funkcije u jednoj tocki: {}'.format(cal.point_derivation(f1, 4, 0.1))); print('Lista brojeva: {}\nIznos derivacija trigonometrijske funkcije: {}'.format(cal.list_derivation(f2, 1, 10, 0.1, True)[0], cal.list_derivation(f2, 1, 10, 0.1, True)[1]))
print('Donja meda: {}, gornja meda: {}'.format(cal.integration(f1, 0, 5, 100)[0],cal.integration(f1, 0, 5, 100)[1])); print('Trapezoidna integracija: {}'.format(cal.trapezoidal_integration(f1, 0, 5, 100)))


plt.plot(cal.list_derivation(f1, -2, 2, 0.1)[0], df1(cal.list_derivation(f1, -2, 2, 0.1)[0])), plt.plot(cal.list_derivation(f1, -2, 2, 0.1)[0], cal.list_derivation(f1, -2, 2, 0.1)[1], 'go'), plt.plot(cal.list_derivation(f1, -2, 2, 0.5)[0], cal.list_derivation(f1, -2, 2, 0.5)[1], 'ro')
plt.title('Derivacija'), plt.xlabel('x'), plt.ylabel("f'(x)"), plt.show()


lista = []
for n in np.linspace(100, 1000, 21):
    plt.plot(n, cal.integration(f3, 0, 1, int(n))[0], 'ro'); plt.plot(n, cal.integration(f3, 0, 1, int(n))[1], 'bo'); plt.plot(n, cal.trapezoidal_integration(f3, 0, 1, int(n)), 'go')
    lista.append(3.66666666666667)
plt.plot(np.linspace(100, 1000, 21), lista)
plt.title('Integracija'), plt.xlabel('Broj koraka'), plt.ylabel('Integral'), plt.show()

print('Donja i gornja meda padajuce funkcije: {}'.format(cal.integration(f4, 0, 1, 100)))
#Ako imamo padajucu funkciju, kao f4, onda zbog nacina na koji numericki racunamo integraciju, donja meda ispadne veca od gornje
#Kod padajuce funkcije krecuci od prve tocke dobivamo pravokutnike iznad grafa, a krecuci od druge tocke, pravokutnkike ispod grafa
#Kod rastuce funkcije je obrnuto