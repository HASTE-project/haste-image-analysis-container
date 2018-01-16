from haste_processing_node.function import process_data
import pickle
import time


def test():
    stream_id = 'delete_me_' + str(time.time())
    print(stream_id)

    # Simulate incoming data originating at the simulator:
    some_bytes = b'this is some bytes'

    # Simulate incoming data originating at the simulator:
    fh = open('haste_processing_node/image_analysis/dummy_image_0.png', 'rb')
    some_bytes = bytes(fh.read())
    fh.close()

    process_data(pickle.dumps({'timestamp': time.time(),
                               'location': (12.34, 56.78),
                               'stream_id': stream_id,
                               'image_length_bytes': len(some_bytes)})
                 + some_bytes)


if __name__ == '__main__':
    test()
