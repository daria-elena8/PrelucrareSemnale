import numpy as np
import matplotlib.pyplot as plt

N = 100
t = np.linspace(0, 1, N)
frequencies = [2, 17, 9]
signal = 4 * np.sin(2 * np.pi * frequencies[0] * t) + \
         0.9 * np.sin(2 * np.pi * frequencies[1] * t) + \
         1.1 * np.sin(2 * np.pi * frequencies[2] * t)

fig, ax = plt.subplots(2, figsize=(10, 6))
ax[0].plot(t, signal)
ax[0].set_title('Semnal compus')
ax[0].set_xlabel('Timp')
ax[0].set_ylabel('Amplitudine')

sig = np.zeros(N, dtype=complex)

for k in range(N):
    for n in range(N):
        sig[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)

ax[1].stem(np.arange(N), np.abs(sig))
ax[1].set_title('Magnitudine')
ax[1].set_xlabel('Frecventa')
ax[1].set_ylabel('Magnitude')

plt.tight_layout()
plt.savefig('manual_fourier_transform.png')
plt.show()
