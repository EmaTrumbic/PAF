def funkc(N):
    rez1 = 0
    rez2 = 5
    for i in range(N):
        rez1 += 1/3
        rez2 -= 1/3
    print('Prvi rezultat: {}, drugi rezultat: {}'.format(rez1, rez2))

funkc(200)
funkc(2000)
funkc(20000)

#Objasnjenje: 1/3 se ne moze zapisati kao potencija broja 2 s cjelobrojnim eksponentom, pa do rezultata dolazimo aproksimacijama.
#Sto vise racunskih operacija napravimo zaredom, to je greska veca te imamo sve vece odstupanje od prave vrijednosti.
#U nasem primjeru, za 200 iteracija rezultat je tocan do na dvanaestu decimalu, za 2000 iteraciju do na desetu, a za 20000 iteracija
#do na osmu decimalu.