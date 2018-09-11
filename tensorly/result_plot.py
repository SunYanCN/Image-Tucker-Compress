import numpy as np
import matplotlib.pylab as plt

Ranks = np.array([50, 100, 200, 300])
PSNR = np.array([25.95, 28.69, 30.8, 38.38])
Time = np.array([0.71, 0.81, 1.42, 1.94])
CR = np.array([0.92, 0.83, 0.59, 0.27])

plt.subplot(3, 1, 1)
plt.plot(Ranks, PSNR, 'ro--')
plt.xlabel('Rank')
plt.ylabel('PSNR')
plt.title('Image Compare PSNR')

plt.subplot(3, 1, 2)
plt.plot(Ranks, CR, 'g*-')
plt.xlabel('Rank')
plt.ylabel('CR')
plt.title('Image Compression Ratio')

plt.subplot(3, 1, 3)
plt.plot(Ranks, Time, 'ys-.')
plt.xlabel('Rank')
plt.ylabel('Time')
plt.title('Decomposition Time')

plt.savefig('result.jpg')
plt.show()
