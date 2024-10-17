import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(-1,1, 400)

fig, axs = plt.subplots(2)
axs[0].plot(t, np.sin(2 * np.pi * 200 * t))
axs[1].plot(t, np.cos(2 * np.pi * 200 * t - np.pi / 2))

plt.savefig('try1.pdf')
plt.show()