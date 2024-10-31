import matplotlib.pyplot as plt
import numpy as np
import os
from time import time
import math

def lab3fft(n):
    matriceFourier = np.zeros((n, n), dtype=complex)
    for linie in range(n):
        for coloana in range(n):
            matriceFourier[linie, coloana] = (1 / np.sqrt(n)) * math.e ** (-2 * np.pi * 1j * linie * coloana / n)
    return matriceFourier

N = [128, 256, 512, 1024, 2048, 4096, 8192]
timplab = []
timpfft = []

if os.path.exists("timpi_lab.npy"):
    timplab = list(np.load("timpi_lab.npy"))
else:
    # calculeaza timpii pentru fiecare N
    for n in N:
        filename = f"matricelab_{n}.npy"
        if not os.path.exists(filename):
            start = time()
            matricelab = lab3fft(n)
            end = time()
            np.save(filename, matricelab)
            timplab.append(end - start)
        else:
            # Placeholder pt dim consistenta
            timplab.append(np.nan)
    # salveaza timpii
    np.save("timpi_lab.npy", timplab)

# calculeaza numpy.fft
for n in N:
    start = time()
    np.fft.fft(np.zeros(n))
    end = time()
    timpfft.append(end - start)


# graficele
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.plot(N, timplab, label="Timp lab3fft")
ax.plot(N, timpfft, label="Timp np.fft")
ax.legend()
fig.savefig('ex1.pdf')
fig.savefig('ex1.png')
plt.show()
