import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import sounddevice as sd

# Amplitude = loudness.
# Frequency = pitch.
# Phase is the point in the wave cycle at which the wave starts, not registered by the human ear directly

# Subpunctul a)
t = np.linspace(0, 1, 1600)
fs = 800
amplitudine = 0.5

semnal = amplitudine *np.sin(2*np.pi * fs * t)
plt.figure()
plt.stem(t, semnal)
plt.show()

rate = 16000
semnalwav = np.int16( semnal * 32767)
wavfile.write('ex3a.wav', rate, semnalwav)

rate, audio = wavfile.read('ex3a.wav')
sd.play(audio, rate)
sd.wait()


