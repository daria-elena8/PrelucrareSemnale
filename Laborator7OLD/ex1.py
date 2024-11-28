import numpy as np
from matplotlib import pyplot as plt

# Definirea dimensiunilor grilei
N1, N2 = 256, 256  # Dimensiunea imaginii
n1 = np.arange(N1)
n2 = np.arange(N2)
n1, n2 = np.meshgrid(n1, n2)

# Generarea funcției
xn = np.sin(2 * np.pi * n1 / N1 + 3 * np.pi * n2 / N2)

# Afișarea imaginii originale
plt.imshow(xn, cmap='gray')
plt.title("Imagine generată")
plt.colorbar()
plt.show()

# FFT 2D
Y = np.fft.fft2(xn)
freq_db = 20 * np.log10(np.abs(Y))

# Afișarea spectrului
plt.imshow(freq_db, cmap='jet')
plt.title("Spectrul de frecvențe")
plt.colorbar()
plt.show()
