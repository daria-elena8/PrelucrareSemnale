import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import sounddevice as sd

rate = 44100
durata = 3

t = np.linspace(0, durata, int(rate * durata))

fs1 = 440
fs2 = 700

sinw1 = np.sin( 2 * np.pi * fs1 * t)
sinw2 = np.sin( 2 * np.pi * fs2 * t)

vector = np.concatenate((sinw1, sinw2))

sd.play(vector, rate)
sd.wait()

# Se aude diferenta in functie de frecventa data
# Frecventa mai mica -> Sunet mai jos
# Frecventa mai mare -> Sunet mai inalt