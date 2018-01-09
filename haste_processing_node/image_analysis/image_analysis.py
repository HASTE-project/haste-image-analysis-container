from PIL import Image
import io
import numpy as np

def extract_image_features(metadata, image_bytes):
    # TODO extract image features here
    image = Image.open(io.BytesIO(image_bytes))
    sum = np.sum(image)
    extracted_features = {
        'image_height': 123,
        'number_of_green_pixels': sum
    }
    return extracted_features
