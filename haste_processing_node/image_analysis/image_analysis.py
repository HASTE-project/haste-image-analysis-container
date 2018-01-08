from PIL import Image
import io


def extract_image_features(metadata, image_bytes):
    # TODO extract image features here

    image = Image.open(io.BytesIO(image_bytes))

    extracted_features = {
        'image_height': 123,
        'number_of_green_pixels': 42
    }
    return extracted_features
