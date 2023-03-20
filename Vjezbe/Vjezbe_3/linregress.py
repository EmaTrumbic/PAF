M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #mjerna jednica Nm
φ = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #mjerna jedinica rad

umnozak_φM = 0
suma_kvadrata = 0

for i in range(len(M)):
    umnozak_φM += φ[i]*M[i]
    suma_kvadrata += (φ[i])**2

umnozak_srednja_vr = umnozak_φM / len(M)
φ_kvadrat_srednja_vr = suma_kvadrata / len(φ)

Dt = umnozak_srednja_vr / φ_kvadrat_srednja_vr

print(Dt)