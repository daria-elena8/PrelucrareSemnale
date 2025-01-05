import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets
from scipy.fft import dctn, idctn


X = datasets.ascent()

Q_jpeg = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 28, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])


# Funcție pentru procesare blocuri 8x8
def process_block(block, q_down):
    y = dctn(block, norm='ortho')  # DCT
    y_jpeg = q_down * np.round(y / q_down)
    x_jpeg = idctn(y_jpeg, norm='ortho')  # transformata inversa DCT
    return x_jpeg

# procesarea pt toata imaginea
h, w = X.shape
X_jpeg = np.zeros_like(X)
q_down = 64
for i in range(0, h, 8):
    for j in range(0, w, 8):
        block = X[i:i+8, j:j+8]
        X_jpeg[i:i+8, j:j+8] = process_block(block, q_down)


fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(X, cmap=plt.cm.gray)
ax[1].imshow(X_jpeg, cmap=plt.cm.gray)

fig.tight_layout()
fig.show()
fig.savefig("ex1.png")

plt.imsave('original.png', X, cmap=plt.cm.gray)
plt.imsave('compressed.png', X_jpeg, cmap=plt.cm.gray)

mse = np.mean((X - X_jpeg) ** 2)
print(f"MSE: {mse}")    #MSE: 20.116134643554688    - comprimare moderata

psnr = 10 * np.log10(255**2 / mse)
print(f"PSNR: {psnr} dB")   #PSNR: 35.095358270410564 dB    - calitate buna
