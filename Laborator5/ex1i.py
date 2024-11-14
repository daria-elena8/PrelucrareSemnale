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

freq = fs * np.arange(n // 2) / n  # frecvențele în Hz

#freqs = np.fft.fftfreq(len(fft_signal), d=1/fs)

# Definim frecvența de tăiere pentru filtrare
cutoff_freq = 0.2  # de exemplu, 0.2 Hz

# Aplicăm filtrarea manuală: păstrăm doar frecvențele sub cutoff_freq
filtered_fft = np.where(abs(freq) > cutoff_freq, 0, fftSig)

# Revenim în domeniul timp cu FFT inversă
filtered_sig = np.fft.ifft(filtered_fft).real

# Vizualizarea semnalului filtrat
plt.figure(figsize=(12, 6))
plt.plot(filtered_sig)
plt.xlabel('ora')
plt.ylabel('nr mașini')
plt.legend()
plt.show()
