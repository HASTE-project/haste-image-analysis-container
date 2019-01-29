import pickle


def split_metadata_and_data(message_bytes):
    # Format is a concatenation of a pickled dictionary, then the image bytes:

    metadata = pickle.loads(message_bytes)  # Note: Bytes past the pickled object’s representation are ignored.

    # metadata = {'stream_id': stream_id,
    #             'timestamp': time.time(),
    #             'location': (12.34, 56.78),
    #             'image_length_bytes': 1000 }
    # See: https://github.com/benblamey/exjobb/blob/master/simulator_no_flask.py#L92

    image_length_bytes = metadata['image_length_bytes']
    image_bytes = message_bytes[-image_length_bytes:]

    return metadata, image_bytes


if __name__ == '__main__':
    # Test
    some_bytes = b'foo'
    metadata, image_bytes = split_metadata_and_data(
        bytearray(
            pickle.dumps(
                {'foo': 123,
                 'bar': 'wibble',
                 'image_length_bytes': len(some_bytes)})
        )
        + some_bytes)

    print(metadata)
    print(image_bytes)
