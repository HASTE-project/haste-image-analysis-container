import cProfile
import datetime

from harmonicPE.daemon import listen_for_tasks

from .haste_storage_client_cache import get_storage_client
from .image_analysis.image_analysis import extract_image_features
from .simulator_messages import split_data_from_simulator

# TODO: This will break on MACOSX (see HIO code for fix)
# import subprocess
# hostname = subprocess.getoutput('hostname')


__processed_message_count = 0

__enable_profiling = False
__profile = None
__PROFILING_BATCH_SIZE = 400  # dump profile stats each N messages (should be 500 but we have a bug elsewhere)
__last_seen_stream_id = None


if __enable_profiling and __profile is None:
    __profile = cProfile.Profile(builtins=False)
    # Don't enable it yet - we'll count all the time the socket is waiting to connect.


def process_data(message_bytes):
    global __processed_message_count, __enable_profiling, __profile, __PROFILING_BATCH_SIZE

    if __enable_profiling:
        __profile.enable()

    print('message received with length bytes: ' + str(len(message_bytes)), flush=True)

    metadata, image_bytes = split_data_from_simulator(message_bytes)

    extracted_features = extract_image_features(metadata, image_bytes)

    metadata['extracted_features'] = extracted_features

    # metadata['containerID'] = hostname

    # Get a storage client for the cache, and use it to save the blob and all metadata:
    stream_id = metadata['stream_id']  # Identifies the data in storage - across all processing nodes.
    timestamp_cloud_edge = metadata['timestamp']

    haste_storage_client = get_storage_client(stream_id)

    haste_storage_client.save(timestamp_cloud_edge,
                              metadata['location'],
                              image_bytes,
                              metadata)

    print('saved to storage!', flush=True)

    __processed_message_count = __processed_message_count + 1

    if __enable_profiling and (__processed_message_count % __PROFILING_BATCH_SIZE == 0):
        # This mechanism is fragile - instead base it on the stream ID
        prof_filename = 'profile_' + datetime.datetime.today().strftime('%Y_%m_%d__%H_%M_%S') + '.prof'
        __profile.disable()
        __profile.dump_stats(prof_filename)
        __profile.clear()
        print('dumped profiling info to: ' + prof_filename, flush=True)


if __name__ == '__main__':
    # Start the daemon to listen for tasks:
    listen_for_tasks(process_data)
