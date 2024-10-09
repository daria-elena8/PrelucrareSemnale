import numpy as np
import matplotlib.pyplot as plt

f = 240
T = 1 / f

t = np.arange(0, 0.1, 1.0 / 200)
n = np.floor(t / T)
y = (2/ T) * (t - n * T)

plt.plot(t, y)
plt.savefig('sawtooth.pdf')
plt.show()