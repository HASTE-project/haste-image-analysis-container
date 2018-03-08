from PIL import Image
import io
import numpy as np
from skimage.feature import greycomatrix, greycoprops
from skimage.filters import laplace

# This constant seems to be specific to the microscope/AZN
GREEN_COLOR_CHANNEL = 2

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


def extract_image_features(metadata, image_bytes):

    if metadata['color_channel'] == GREEN_COLOR_CHANNEL:
        image = np.array(Image.open(io.BytesIO(image_bytes)))

        extracted_features = {
            # numpy's special uint64 type (see: https://docs.scipy.org/doc/numpy/reference/arrays.scalars.html)
            # is not BSON-encodable for mongoDB, convert to python3 int.
            'sum_of_intensities': int(np.sum(image)),
            'correlation': __corr(image),
            'laplaceVariance': __laplace_variance(image)
        }
        return extracted_features
    else:
        return {}


if __name__ == '__main__':
    # Test extraction with the dummy image
    fh = open('dummy_image_0.tif', 'rb')
    image_bytes = bytes(fh.read())
    fh.close()

    extracted_features = extract_image_features({'location': (12.34, 56.78),
                                                 'image_length_bytes': len(image_bytes)}, image_bytes)
    print(extracted_features)
