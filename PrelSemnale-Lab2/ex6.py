import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,1, 300)
fs = 800
a = np.sin(2 * np.pi * fs / 2 *t)
b = np.sin(2 * np.pi * fs / 4 *t)
c = np.sin(2 * np.pi * 0 *t) # sau np.sin(0) sau c=0


fig, ax = plt.subplots(3)
ax[0].plot(t, a)
ax[1].plot(t, b)
ax[2].plot(t, c)

plt.show()
plt.savefig('ex6.pdf')

# Primul semnal are cea mai mare frecventa, deci se repeta cel mai des
# Al doilea se repeta la jumatate fata de primul
# Al 3-lea semnal este constant