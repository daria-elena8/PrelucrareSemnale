import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dctn, idctn
from skimage import color

# imag exemplu RGB
imag = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

# conversie
imag_ycbcr = color.rgb2ycbcr(imag)

canale = [dctn(imag_ycbcr[..., i], norm='ortho') for i in range(3)]
mat = 64
canaleComprim = [mat * np.round(c / mat) for c in canale]
canaleRemade = [idctn(c, norm='ortho') for c in canaleComprim]

# reconstructie
ycbcrComprim = np.stack(canaleRemade, axis=-1)
rgbComprim = np.clip(color.ycbcr2rgb(ycbcrComprim), 0, 255).astype(np.uint8)

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(imag)
plt.title("original")

plt.subplot(122)
plt.imshow(rgbComprim)
plt.title("compressed")

plt.tight_layout()
plt.show()
