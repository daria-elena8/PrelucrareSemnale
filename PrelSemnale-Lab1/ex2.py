import numpy as np
import matplotlib.pyplot as plt

# Subpunctul a)
t = np.linspace(-1, 1, 1600)
fig, ax = plt.subplots()
plt.stem(t, np.sin(2 * np.pi * 800 * t))
ax.set_title('a)')
plt.savefig('ex2A.pdf')
plt.show()


t = np.linspace(0, 3, 2400)
fig, ax = plt.subplots()
plt.stem(t, np.sin(2 * np.pi * 800 * t))
ax.set_title('b)')
plt.savefig('ex2B.pdf')
plt.show()
