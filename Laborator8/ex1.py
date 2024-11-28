import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg

N = 100
t = np.linspace(0, 1, N)

trend = 0.2 * t**2 - 0.8 * t + 2
season = 2 * np.sin(2 * np.pi * t) + 1.4 * np.cos(4 * np.pi * t)
noise = np.random.normal(loc=0, scale=0.5, size=N)
serie = trend + season + noise

fig, ax = plt.subplots(4, 1, figsize=(10, 12))

ax[0].plot(t, trend)
ax[1].plot(t, season)
ax[2].plot(t, noise)
ax[3].plot(t, serie)

fig.tight_layout()
fig.show()
fig.savefig("ex1a.png")

# autocorelatie -- b)
autocorr = np.correlate(serie, serie, mode='full')
# pastram doar partea poz
autocorr = autocorr[autocorr.size // 2:]
autocorr /= autocorr[0]

plt.figure()
plt.plot(autocorr)
plt.grid()
plt.savefig("ex1b.png")
plt.show()

# model AR -- c)
p = 40
model = AutoReg(serie, lags=p).fit()
predict = model.predict(start=p, end=N-1)

plt.figure()
plt.plot(t[p:], predict)
plt.grid()
plt.savefig("ex1c.png")
plt.show()
