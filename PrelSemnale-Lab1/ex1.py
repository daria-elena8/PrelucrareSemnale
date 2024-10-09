import numpy as np
import matplotlib.pyplot as plt

# Subpunctul a)
t = np.arange(0, 0.03, np.random.uniform(0.0001,0.009))

# Subpunctul b)
fig, axs = plt.subplots(3, 1)
fig.suptitle('Exercitiul 1 (a,b) ')

x = np.cos(520 * np.pi * t + np.pi / 3)
y = np.cos(280 * np.pi * t - np.pi / 3)
z = np.cos(120 * np.pi * t + np.pi / 3)

axs[0].plot(t, x)
axs[1].plot(t, y)
axs[2].plot(t, z)

axs[0].set_ylabel('x(t)')
axs[1].set_ylabel('y(t)')
axs[2].set_ylabel('z(t)')

plt.savefig('ex1AB.pdf')

plt.show()

# Subpunctul c)

fig, axs = plt.subplots(3)

t = np.arange(0, 0.8, 0.8/200)

xc = np.cos(520 * np.pi * t + np.pi / 3)
yc = np.cos(280 * np.pi * t - np.pi / 3)
zc = np.cos(120 * np.pi * t + np.pi / 3)

axs[0].stem(t, xc)
axs[1].stem(t, yc)
axs[2].stem(t, zc)

axs[0].set_ylabel('x(t)')
axs[1].set_ylabel('y(t)')
axs[2].set_ylabel('z(t)')

plt.savefig('ex1C.pdf')
plt.show()