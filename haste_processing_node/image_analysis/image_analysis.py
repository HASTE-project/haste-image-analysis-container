from PIL import Image
import io
import numpy as np
from skimage import greycomatrix, greycoprops


def corr(im):

    glcm = greycomatrix(im.astype('uint8'), [1], [0], normed=True)
    stats = greycoprops(glcm, 'correlation')
    return stats


def extract_image_features(metadata, image_bytes):

    # TODO extract image features here
    image = Image.open(io.BytesIO(image_bytes))

    image_sum = np.sum(image)
    image_correlation = corr(image)

    extracted_features = {
        'image_height': 123,
        'number_of_green_pixels': image_sum,
        'correlation': image_correlation
    }
    return extracted_features
