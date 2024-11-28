import numpy as np
from matplotlib import pyplot as plt

# dim grilei
dim1, dim2 = 128, 128
n1 = np.linspace(0, 1, dim1)
n2 = np.linspace(0, 1, dim2)

n1, n2 = np.meshgrid(n1, n2)

def funcA(n1, n2):
    return np.sin(2 * np.pi * n1 + 3 * np.pi * n2)

def funcB(n1, n2):
    return np.sin(4 * np.pi * n1) + np.cos(6 * np.pi * n2)

fig, ax = plt.subplots(2, 2, figsize=(12, 10))

# sin(2pi* n1 + 3pi* n2)
fn = funcA(n1, n2)
x = np.fft.fftshift(np.fft.ifft2(fn))
ax[0][0].imshow(fn, cmap='gray')
# afisare spectru A
im = ax[0][1].imshow(np.abs(x), cmap='jet')


# sin(4pi* n1) + cos(6pi* n2)
fn = funcB(n1, n2)
x = np.fft.fftshift(np.fft.ifft2(fn))
ax[1][0].imshow(fn, cmap='gray')
# afisare spectru B
im = ax[1][1].imshow(np.abs(x), cmap='jet')

plt.savefig("ex1AB.png")
plt.show()
