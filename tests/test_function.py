import pytest
from haste_processing_node.function import process_data, extract_image_features
import pickle
import time


def test_process_data():
    stream_id = 'delete_me_' + str(time.time())
    print(stream_id)

    # Simulate incoming data originating at the simulator:
    some_bytes = b'this is some bytes'

    # Simulate incoming data originating at the simulator:
    fh = open('haste_processing_node/image_analysis/dummy_image_0.tif', 'rb')
    some_bytes = bytes(fh.read())
    fh.close()

    process_data(pickle.dumps({'timestamp': '1234',
                               'location': (12.34, 56.78),
                               'stream_id': stream_id,
                               'image_length_bytes': len(some_bytes)})
                 + some_bytes)


def test_extract_image_features():
    # Test extraction with the dummy image
    fh = open('tests/foo-16bit.tif', 'rb')
    image_bytes = bytes(fh.read())
    fh.close()

    extracted_features = extract_image_features({'location': (12.34, 56.78),
                                                 'image_length_bytes': len(image_bytes)}, image_bytes)
    print(extracted_features)
