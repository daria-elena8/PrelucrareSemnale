import numpy as np
import matplotlib.pyplot as plt
import pickle

with open("date_sig.pkl", "rb") as f1:
    sig = pickle.load(f1)
with open("date_fftSig.pkl", "rb") as f2:
    fftSig = pickle.load(f2)

fs = 1/3600
n = len(sig)
t = fs *np.linspace(0, n // 2, n // 2) / n


# f) cele mai mari 4 valori

freq = fs * np.arange(n // 2) / n  # frecvențele în Hz

top_index = np.argsort(fftSig)[-4:][::-1]
top_freq = freq[top_index]
top_amp = fftSig[top_index]

for i in range(4):
    print(f"Frecvența {i+1}: {top_freq[i]:.4f} Hz, Amplitudine: {top_amp[i]:.4f}")

# reprezentare FFT
fig, ax = plt.subplots()
ax.plot(freq, fftSig)
ax.plot(top_freq, top_amp, "ro")  # marcăm frecvențele principale
plt.show()
fig.savefig('ex1f.png')
