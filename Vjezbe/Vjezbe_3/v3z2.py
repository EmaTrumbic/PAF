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