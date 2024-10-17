import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(-1, 1, 200)

sinw = np.sin( 2* np.pi * 600 * t)
saww = signal.sawtooth(2 * np.pi * 5 * t)
ambele = sinw + saww

fig, ax = plt.subplots(3)
ax[0].plot(t, sinw)
ax[0].set_title('Semnal sinusoidal')
ax[1].plot(t, saww)
ax[1].set_title('Semnal sawtooth')
ax[2].plot(t, ambele)
ax[2].set_title('Semnalul adunat')

plt.tight_layout() # Se scrie peste fara
plt.savefig('ex4.pdf')
plt.show()