import logging
import os

import yaml
from google.cloud import storage
from google.cloud.exceptions import Forbidden


def _update_env_from_yaml():
    try:
        # local
        with open('./env.yaml') as f:
            os.environ.update(yaml.load(f))
    except FileNotFoundError as e:
        # Google Cloud Functions
        pass


def _update_env_from_gcs():
    bucket_name = 'bucket_name'

    try:
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = storage.Blob('env.yaml', bucket)
        yaml.load(blob.download_as_string())
        os.environ.update(yaml.load(blob.download_as_string()))
    except Forbidden:
        logging.error('Cannot load environments from Google Cloud Storage.')
        pass


def update_environ():
    _update_env_from_yaml()
    # _update_env_from_gcs()
