import matplotlib.pyplot as plt
import numpy as np

t= np.linspace ( 0, 1, 300)
fs = 1000
a = np.sin(2 * np.pi * fs * t)
a1 = a[::4]
t1 = t[::4]
fig, ax = plt.subplots(3)
ax[0].plot(t,a)
ax[1].plot(t1,a1)

#a) se observa ca se pierde din calitatea semnalului
# acest lucru este de inteles, avem mai putine puncte ->
# semnal de calitate slaba

a2 = a[1::4]
t2 = a[1::4]
ax[2].plot(t2,a2)
plt.show()
plt.savefig('ex7ab.pdf')

# b) S-a pierdut din exactitatea esantionarii foarte mult
# Ar fi trebuit sa fie o diferenta de faza
# avand in vedere ca incepe cu un element mai tarziu fata
# de semnalul anterior, dar se pierde foarte mult
# din semnal