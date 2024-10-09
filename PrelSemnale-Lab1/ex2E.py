import numpy as np
import matplotlib.pyplot as plt

semnal = np.random.rand(128, 128)

plt.imshow(semnal)
plt.savefig('ex2E.pdf')
plt.show()
