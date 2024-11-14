import numpy as np
from scipy.fft import fft, ifft

n = int(input("n = "))
p = np.random.randint(0, 10, n+1)
q = np.random.randint(0, 10, n+1)

r1 = np.convolve(p, q)
var1 = np.zeros(2*n + 1)

for i in range(len(p)):
    for j in range(len(q)):
        var1[i + j] += p[i] * q[j]


pfft = fft(p, 2*n + 1)
qfft = fft(q, 2*n + 1)
r2 = pfft *qfft
var2 = np.real(np.fft.ifft(r2))

print("p(x): ", p)
print("q(x): ", q)
print("produs convolutie: ", var1)
print("produs fft: ", var2)

