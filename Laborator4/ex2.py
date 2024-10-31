import matplotlib.pyplot as plt
import numpy as np

fs = 15     # -> frecv sub Nyquist pt toate semnalele
f1 = 8
f2 = f1 + fs    # va suferi aliere
f3 = f1 + 3*fs  # va suferi aliere

continuu = np.linspace(0, 1, 1000, endpoint=False)
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