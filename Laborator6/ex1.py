import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(100)

fig, ax = plt.subplots(4)
ax[0].plot(x)

m1 = x*x
m2 = m1 * m1

ax[1].plot(m1)
ax[2].plot(m2)
ax[3].plot(m2 * m2)

# semnalul se netezeste pentru fiecare modificare
plt.show()
fig.savefig("ex1.pdf")
