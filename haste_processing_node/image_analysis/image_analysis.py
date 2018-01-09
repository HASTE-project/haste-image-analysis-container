from PIL import Image
import io
import numpy as np
from skimage.feature import greycomatrix, greycoprops


def corr(im):
    # Needs a 2D image

    glcm = greycomatrix(im.astype('uint8'), [1], [0], normed=True)
    stats = greycoprops(glcm, 'correlation')
    return np.mean(stats)


def extract_image_features(metadata, image_bytes):

    # TODO extract image features here
    image = np.array(Image.open(io.BytesIO(image_bytes)))

    image_sum = np.sum(image[:, :, 0])
    image_correlation = corr(image[:, :, 0])

    extracted_features = {
        'image_height': 123,
        'number_of_green_pixels': image_sum,
        'correlation': image_correlation
    }
    return extracted_features
