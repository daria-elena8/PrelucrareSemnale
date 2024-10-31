import matplotlib.pyplot as plt
import numpy as np

fs = 10     # -> frecv initiala
f1 = 6
f2 = f1 + fs    # nu va suferi aliere
f3 = f1 + 2*fs  # nu va suferi aliere
fs = 2 * (f1 + 2 * fs)  # Creștem fs pentru a fi mult peste frecvențele semnalelor.

continuu = np.linspace(0, 1, 600, endpoint=False)
discret = np.linspace(0,1, fs, endpoint=False)

freq = [f1,
        f2,
        f3]

fig, ax = plt.subplots(3)
for i, f in enumerate(freq):
    sig1 = np.sin( 2 * np.pi * f * continuu)
    sig2 = np.sin( 2 * np.pi * f * discret)

    ax[i].plot(continuu, sig1)
    ax[i].stem(discret, sig2)


fig.savefig('ex2.pdf')
fig.savefig('ex2.png')
plt.show()