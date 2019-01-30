from PIL import Image
import io
import numpy as np
from skimage.feature import greycomatrix, greycoprops
from skimage.filters import laplace



def __laplace_variance(im):
    lap_var = laplace(im).var()
    return lap_var


def __corr(im):
    # Needs a 2D image
    if len(im.shape) > 2:
        raise Exception('Only works with 2D images')

    glcm = greycomatrix(im.astype('uint8'), [1], [0], normed=True)
    stats = greycoprops(glcm, 'correlation')
    return np.mean(stats)


def extract_features(image_bytes):
    image = np.array(Image.open(io.BytesIO(image_bytes)))
    extracted_features = {
        # numpy's special uint64 type (see: https://docs.scipy.org/doc/numpy/reference/arrays.scalars.html)
        # is not BSON-encodable for mongoDB, convert to python3 int.
        'sum_of_intensities': int(np.sum(image)),
        'correlation': __corr(image),
        'laplaceVariance': __laplace_variance(image)
    }
    return extracted_features


