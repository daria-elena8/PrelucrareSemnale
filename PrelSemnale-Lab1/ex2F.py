import numpy as np
import matplotlib.pyplot as plt
n = 128
tabla = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if (i // 8 + j // 8) % 2 == 0:
            tabla[i, j] = 1

plt.imshow(tabla)
plt.savefig('TablaSah.pdf')
plt.show()
