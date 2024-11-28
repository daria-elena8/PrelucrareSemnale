import numpy as np
from matplotlib import pyplot as plt

# dim matrice
dim = 64


def funcC(dim):
    mat = np.zeros((dim, dim))
    mat[0][5] = mat[0][dim-5] = 1
    return mat

def funcD(dim):
    mat = np.zeros((dim, dim))
    mat[5][0] = mat[dim-5][0] = 1
    return mat

def funcE(dim):
    mat = np.zeros((dim, dim))
    mat[5][5] = mat[dim-5][dim-5] = 1
    return mat

fig, ax = plt.subplots(3, 2, figsize=(9, 9))

# func C
fn = funcC(dim)
x = np.fft.fftshift(np.fft.fft2(fn))

ax[0][0].imshow(fn, cmap='gray')
im = ax[0][1].imshow(np.abs(x), cmap='PuRd')

# func D
fn = funcD(dim)
x = np.fft.fftshift(np.fft.fft2(fn))

ax[1][0].imshow(fn, cmap='gray')
im = ax[1][1].imshow(np.abs(x), cmap='PuRd')

# func E
fn = funcE(dim)
x = np.fft.fftshift(np.fft.fft2(fn))

ax[2][0].imshow(fn, cmap='gray')
im = ax[2][1].imshow(np.abs(x), cmap='PuRd')

plt.tight_layout()
plt.savefig("ex1CDE.png")
plt.show()
