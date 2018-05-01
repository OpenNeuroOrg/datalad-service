import json
import pytest
from datalad_service.s3 import upload
from .dataset_fixtures import *

def test_celery():
    annex_path = 'datalad'
    task = upload.delay(annex_path, DATASET_ID, 'tag', False)
    assert task is not None