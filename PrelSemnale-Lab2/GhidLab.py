import scipy.io.wavfile
import numpy as np
import sounddevice as sd

rate = 44100
fs = 500
duration = 2

t = np.linspace(0, duration, int(rate * duration))

amplitude = 120
data = amplitude * np.sin(2 * np.pi * fs * t)

scipy.io.wavfile.write('numee.wav', rate, data.astype(np.int16))

rate, myarray = scipy.io.wavfile.read('numee.wav')
sd.play(myarray, rate)
sd.wait()