import numpy as np
import matplotlib.pyplot as plt
import pickle


# e) Un semnal prezinta o componenta continua daca are media diferita de 0.
# Asta se poate vedea daca apar peak uri in reprezentarea FFT.
# Aici apar peak uri -> avem comp continua.
# Scapam de comp continua prin scaderea mediei semnalului

with open("date_sig.pkl", "rb") as f1:
    sig = pickle.load(f1)
with open("date_fftSig.pkl", "rb") as f2:
    fftSig = pickle.load(f2)

fs = 1/3600
n = len(sig)
t = fs *np.linspace(0, n // 2, n // 2) / n

media_sig = np.mean(sig)
sig2 = sig - media_sig

fftSig2 = np.fft.fft(sig2)
fftSig2 = abs(fftSig2 / len(sig2))
fftSig2 = fftSig2[:len(fftSig2) // 2]

fig, ax = plt.subplots()
ax.plot(t, fftSig2)
plt.show()
fig.savefig('ex1e.png')
