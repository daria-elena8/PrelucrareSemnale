import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 300)
fig, ax = plt.subplots()
plt.plot( t, np.sign(np.sin(2 *np.pi * 300 * t)))
ax.set_title('c)')
plt.savefig('ex2C.pdf')
plt.show()

