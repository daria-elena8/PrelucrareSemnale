import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets
from scipy.fft import dctn, idctn

X = datasets.ascent()
# Funcție pentru procesare blocuri 8x8
def process_block(block, q_down):
    y = dctn(block, norm='ortho')  # DCT
    y_jpeg = q_down * np.round(y / q_down)
    x_jpeg = idctn(y_jpeg, norm='ortho')  # transformata inversa DCT
    return x_jpeg

# Prag MSE impus de utilizator
mseImpus = float(input("Introduceți pragul MSE dorit: "))
dif = 5.0  # diferenta maxima tolerata
q_down = 64


def comprimareMse(X, q_down, target_mse, dif):
    h, w = X.shape
    step = 4
    X_jpeg = np.zeros_like(X)
    mse = float('inf')  # MSE inițial mare

    while abs(mse - target_mse) > dif:
        for i in range(0, h, 8):
            for j in range(0, w, 8):
                block = X[i:i + 8, j:j + 8]
                X_jpeg[i:i + 8, j:j + 8] = process_block(block, q_down)

        mse = np.mean((X - X_jpeg) ** 2)
        if mse > target_mse:    # ajustam q_down
            q_down += step
        else:
            q_down -= step
        q_down = max(1, q_down)  # pt 0 sau neg

    return X_jpeg, mse, q_down


X_jpeg, mse, q_down = comprimareMse(X, q_down, mseImpus, dif)



fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(X, cmap=plt.cm.gray)
ax[1].imshow(X_jpeg, cmap=plt.cm.gray)

fig.tight_layout()
fig.show()
fig.savefig("ex1.png")

plt.imsave('ex3original.png', X, cmap=plt.cm.gray)
plt.imsave('ex3compressed.png', X_jpeg, cmap=plt.cm.gray)

print(f"Prag MSE atins: {mse:.2f} cu q_down={q_down}")
