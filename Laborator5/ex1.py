import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import pickle

#   a)
#   o data/ora -> 60 sec * 60 min = 3600
#   frecventa = 1/3600 = 0.0002777777777777778 Hz
#   print(1/3600)
fs = 1/3600

#   b) 18.288 ore -> 18288/24 = 762 ore
#   c) pentru esantionare corecta -> cel putin 1/2
#   din frecventa de esantionare
#   pentru frecventa optima -> cel mult 1/2
#   din frecventa de esantionare
#   => frecv Nyquist = 1/2 * 0.0002777777777777778 Hz
#   => 0.0001388888888888889 Hz

dateTren = {}
with open("Train.csv.xls") as train:
    reader = csv.DictReader(train, delimiter = ',')
    for row in reader:
        dateTren[int(row['ID'])] = {'datetime': datetime.strptime(row['Datetime'], "%d-%m-%Y %H:%M"), 'count': int(row['Count'])}


# d)
sig = np.genfromtxt('Train.csv.xls', delimiter=',', skip_header=1)
sig = sig[:,2]
print(sig)

n = len(sig)

fftSig = np.fft.fft(sig)
fftSig = abs(fftSig/n)
fftSig = fftSig[:n//2]

with open("date_sig.pkl", "wb") as f1:
    pickle.dump(sig, f1)
with open("date_fftSig.pkl", "wb") as f2:
    pickle.dump(fftSig, f2)

t = fs *np.linspace(0, n // 2, n // 2) / n

fig, ax = plt.subplots()
ax.plot(t, fftSig)
plt.show()
fig.savefig('ex1d.png')
