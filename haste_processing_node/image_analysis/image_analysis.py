from PIL import Image
import io
import numpy as np
from skimage.feature import greycomatrix, greycoprops
from skimage.filters import laplace


def laplaceVariance(im):
    lap_var = laplace(im).var()
    return lap_var


def corr(im):
    # Needs a 2D image
    if len(im.shape) > 2:
        print('Only works with 2D images')
        return 0

    glcm = greycomatrix(im.astype('uint8'), [1], [0], normed=True)
    stats = greycoprops(glcm, 'correlation')
    return np.mean(stats)


def extract_image_features(metadata, image_bytes):

    image = np.array(Image.open(io.BytesIO(image_bytes)))

    extracted_features = {
        'sum_of_intensities': np.sum(image),
        'correlation': corr(image),
        'laplaceVariance': laplaceVariance(image)
    }
    return extracted_features
