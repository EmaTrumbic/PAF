#Prvi dio zadatka
print('Ocekivani rezultat: 5.0 - 4.935 = 0.065')
print('Dobiveni rezultat: 5.0 - 4.935 = {}'.format(5.0-4.935))
#Objasnjenje: svaki broj se mora zapisati u binarnom zapisu da bi se spremio u memoriju, pa se samo razlomci oblika 2^{-n},
#gdje je n prirodan broj, mogu konacno zapisati, a sve ostalo je aproksimacija.


#Drugi dio zadatka
suma = 0.1 + 0.2 + 0.3
print('Suma je: {}'.format(suma))
print('Je li suma jednaka 0.6: {}'.format(suma==0.6))
#Objasnjenje: ovi brojevi se zapisuju kao razlomci oblika 1/10, 1/5 i 3/10. Nikoji od ovih razlomaka se ne moze zapisati u obliku
#2^{-n}, pa zbrajamo njihove aproksimacije, te dobijemo rezultat koji je priblizno jednak 3/5.