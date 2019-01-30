from haste_storage_client.core import HasteStorageClient, OS_SWIFT_STORAGE, TRASH

from haste.windowed_conformal_model.conformal_interestingness_model import ConformalInterestingnessModel

import json
import os.path
import urllib.request

haste_storage_clients_az_lnp = {}
haste_storage_clients_vironova = {}


def __get_magic_haste_client_config_from_server(host):
    print('attempting to read config info from ' + host + '...', flush=True)
    t = 'w0rj540vhw8dx0ng0t6nw8cghp'
    url = 'http://' + host + ':27000/' + t + '/haste_storage_client_config.json'
    stream = urllib.request.urlopen(url, timeout=2)
    config = stream.read()
    config = config.decode('utf-8')
    config = json.loads(config)
    return config


def __get_haste_storage_client_config():
    # If a local config file exists, use it:
    json_config = os.path.expanduser('~/.haste/haste_storage_client_config.json')
    if os.path.isfile(json_config):
        return None  # Client will attempt to read config from this file if passed 'None'.

    # Otherwise, use the auto-configuration server:
    # There is no DNS for SNIC, so hostnames won't work here. (unless /etc/hosts is updated inside the container).
    for host in ['192.168.1.28',  # metadata-db-prod (private)
                 '130.239.81.96',  # metadata-db-prod (public)
                 '127.0.0.1']:
        try:
            return __get_magic_haste_client_config_from_server(host)
        except Exception as e:
            print(e)
            print('...failed')
    print('failed reading config from all locations', flush=True)


def get_storage_client_az_lnp(stream_id):
    # For the Vironova dataset, streamed from microscope.
    if stream_id not in haste_storage_clients_az_lnp:
        haste_storage_client_config = __get_haste_storage_client_config()

        model = ConformalInterestingnessModel()

        client = HasteStorageClient(stream_id,
                                    config=haste_storage_client_config,
                                    interestingness_model=model,
                                    storage_policy=[(0.5, 1.0, OS_SWIFT_STORAGE)])  # discard blobs which don't match the policy.

        print('creating client for stream ID: ' + stream_id, flush=True)

        haste_storage_clients_az_lnp[stream_id] = client

    # TODO: only cache N clients.

    return haste_storage_clients_az_lnp[stream_id]


def get_storage_client_vironova(stream_id):
    if stream_id not in haste_storage_clients_vironova:
        haste_storage_client_config = __get_haste_storage_client_config()

        # Default to 1.0
        model = None

        client = HasteStorageClient(stream_id,
                                    config=haste_storage_client_config,
                                    interestingness_model=model,
                                    storage_policy=[(0.0, 1.0, OS_SWIFT_STORAGE)])  # discard blobs which don't match the policy.

        print('creating client for stream ID: ' + stream_id, flush=True)

        haste_storage_clients_az_lnp[stream_id] = client

    # TODO: only cache N clients.

    return haste_storage_clients_az_lnp[stream_id]


if __name__ == '__main__':
    # Test
    config = __get_haste_storage_client_config()
    print(config)
