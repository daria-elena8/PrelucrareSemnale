import matplotlib.pyplot as plt
import numpy as np
import math

t = np.linspace(0, 1, 200)
fs = 10
sig = np.sin( 2 * np.pi * fs * t )
w = 2
semnal = sig * np.exp(-2 * np.pi * 1j * w * t)

dist = np.abs(semnal)
calcDist = (dist - np.max(dist)) / (np.min(dist - np.max(dist)))
culori = plt.cm.viridis(calcDist)

fig, ax = plt.subplots( 2, figsize = (10, 20))

ax[0].plot(t, sig)
ax[1].scatter(semnal.real, semnal.imag, c=culori)
ax[1].set_xlim([-1, 1])
ax[1].set_ylim([-1, 1])

plt.show()
plt.tight_layout()
plt.savefig('ex2a.pdf')
plt.savefig('ex2a.png')

fig, ax = plt.subplots( 2,2 , figsize = (10, 10))
freq = [2, 6, 13, 15]

for i, fr in enumerate(freq):
    semnalNou = sig * np.exp(-2 * np.pi * 1j * fr * t)
    dist = np.abs(semnal)
    calcDist = (dist - np.max(dist)) / (np.min(dist - np.max(dist)))
    culori = plt.cm.viridis(calcDist)
    ax[i//2, i%2].scatter(semnalNou.real, semnalNou.imag, c=culori)

plt.savefig('ex2b.pdf')
plt.savefig('ex2b.png')
#plt.show()
