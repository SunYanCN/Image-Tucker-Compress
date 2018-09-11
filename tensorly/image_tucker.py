import numpy as np
import tensorly as tl
from tensorly.decomposition import tucker

random_state = 1234

from PIL import Image
import matplotlib.pylab as plt

import time

from skimage.measure import compare_psnr

im = Image.open("Lenna.png")
print('Image Mode and Size：' + str(im.mode) + ',' + str(im.size))

data = np.array(im)
print('Image Shape：' + str(data.shape))

data_float = data.astype(np.float32)

time0 = time.time()

tucker_ranks = [50, 50, 3]
core, factors = tucker(data_float, rank=tucker_ranks, init='svd', random_state=random_state, verbose=True)
data_reconstruction = tl.tucker_to_tensor(core, factors)

print('Image Reconstruction Shape：' + str(data_reconstruction.shape))


def convert2uin8(tensor):
    im = tl.to_numpy(tensor)
    im -= im.min()
    im /= im.max()
    im *= 255
    return im.astype(np.uint8)


im_reconstruction = convert2uin8(data_reconstruction)

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
ax.set_axis_off()
ax.imshow(im)
ax.set_title('Original')

ax = fig.add_subplot(1, 2, 2)
ax.set_axis_off()
ax.imshow(im_reconstruction)
ax.set_title('Tucker')

plt.tight_layout()
plt.savefig(str(tucker_ranks[0]) + '.jpg')
plt.show()

size_decomposition = sum([factor.size for factor in factors]) + core.size
compression_ratio = 1 - (1.0 * size_decomposition / data.size)
print('Image Compression Ratio：' + str(compression_ratio))

psnr = compare_psnr(data, im_reconstruction)
print('Image Compare PSNR：' + str(psnr))

print('Decomposition Time：' + str(time.time() - time0))
