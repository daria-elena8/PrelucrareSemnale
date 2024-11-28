from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

# imagine
X = misc.face(gray=True)

# transf fourier
Y = np.fft.fft2(X)
Y_shifted = np.fft.fftshift(Y)  # mutam frecv joase la mijloc pt masca

# dim pt imagine si centru
rows, cols = X.shape
center_row, center_col = rows // 2, cols // 2

# prag taiere
freq_cutoff = 40

# pastrez frecv joase
mask = np.zeros_like(Y_shifted)
mask[center_row - freq_cutoff:center_row + freq_cutoff,
     center_col - freq_cutoff:center_col + freq_cutoff] = 1

# aplicam masca pe fourier
Y_compressed = Y_shifted * mask

# inv fourier -> imag comprimata
Y_compressed_shifted_back = np.fft.ifftshift(Y_compressed)
X_compressed = np.fft.ifft2(Y_compressed_shifted_back) 
X_compressed = np.real(X_compressed)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(X, cmap=plt.cm.gray)
ax[1].imshow(X_compressed, cmap=plt.cm.gray)

fig.tight_layout()
fig.show()
fig.savefig("ex2.png")


