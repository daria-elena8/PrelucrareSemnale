import matplotlib.pyplot as plt
import numpy as np
import math


n = 8
matriceFourier = np.zeros((n,n), dtype = complex)

for linie in range(n):
    for coloana in range(n):
        matriceFourier[linie, coloana] =  (1 / np.sqrt(n)) * math.e**(-2 * np.pi * 1j *linie * coloana / n)

# F**H * F sa fie allclose de I sau F**H * F - I sa fie allclose de 0
conjugata = np.conjugate(matriceFourier).T
I = np.eye(n)
produs = np.dot(conjugata, matriceFourier)
print(f"Verificare unitaritate matrice: {np.allclose(produs, I)}")

fig, ax = plt.subplots( n, figsize = (15, 15))

for linie in range(n):
    ax[linie].plot(matriceFourier.real[linie], marker='.')
    ax[ linie].plot(matriceFourier.imag[linie], marker='*')


plt.show()
plt.tight_layout()
plt.savefig("ex1.pdf")
plt.savefig("ex1.png")
