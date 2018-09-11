import numpy as  np
from tensorcomlib.decomposition import tucker as tk
from tensorcomlib.tensor import tensor

np.random.seed(1234)

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

tucker_ranks = [200, 200, 3]

tensor_data = tensor(data)
U, core = tk.hooi(tensor_data, ranks=tucker_ranks, tol=10e-8, print_enable=True, init='hosvd', plot_enable=True)
data_reconstruction = tk.tucker2tensor(U, core)

print('Image Reconstruction Shape：' + str(data_reconstruction.shape))


def convert2uin8(tensor):
    im = tensor.data
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

size_decomposition = np.sum([np.size(i) for i in U]) + core.size()
compression_ratio = 1 - (1.0 * size_decomposition / data.size)
print('Image Compression Ratio：' + str(compression_ratio))

psnr = compare_psnr(data, im_reconstruction)
print('Image Compare PSNR：' + str(psnr))

print('Decomposition Time：' + str(time.time() - time0))
