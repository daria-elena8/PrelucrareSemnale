import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 400)

a = 10
fs = 1
faze = [0, np.pi/4, np.pi/2, np.pi]
plt.figure(figsize=(10, 6))

for i in faze:
    sig = a * np.sin(2 * np.pi * fs * t + i)
    plt.plot(t, sig, label=f"{i:}")

plt.legend()

plt.savefig('ex2.pdf')
plt.show()

##########################
a=10
valSNR = [0.1, 1, 10, 100]
faza = np.pi / 4

sig = a * np.sin(2 * np.pi* fs * t + faza)
zgomot = np.random.normal(0, 0.8, len(t))

normaSig = np.linalg.norm(sig)
normaZgomot = np.linalg.norm(zgomot)

plt.figure(figsize=(12,8))

for i in valSNR:
    gamma = normaSig / (np.sqrt(i) * normaSig)

    sigZgomot = sig + gamma * zgomot
    plt.plot(t, sigZgomot, label=f"SNR {i}")

plt.legend()
plt.savefig('ex2Zgomot.pdf')
plt.show()