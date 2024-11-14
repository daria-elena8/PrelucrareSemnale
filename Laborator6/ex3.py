import numpy as np
import matplotlib.pyplot as plt

def dreptunghi(n):
    return np.ones(n)

def hanning(n):
    return np.hanning(n)

f = 100
phi = 0

fs = 150
dimFereastra = 200
t = np.arange(dimFereastra)/fs

sin = np.sin( 2 * np.pi *f * t + phi)

sinDreptunghiular = sin * dreptunghi(dimFereastra)
sinHanning = sin * hanning(dimFereastra)

fig, ax = plt.subplots(3)
ax[0].plot(t, sin)
ax[1].plot(t, sinDreptunghiular)
ax[2].plot(t, sinHanning)

plt.show()
fig.savefig("ex3.pdf")

