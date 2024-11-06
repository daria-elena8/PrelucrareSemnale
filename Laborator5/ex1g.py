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

# g

fs = 1200
# 30 zile * 24 ore
samples = 30 * 24

start_index = 2  # al 3 lea sample
traffic_month = sig[start_index:start_index + samples]

# Graficul
plt.plot(traffic_month)
plt.xlabel('ora')
plt.ylabel('nr mașini')
plt.show()