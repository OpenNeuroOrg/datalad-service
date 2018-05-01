import os
from .datalad import DataladStore
import datalad
from celery import Celery

app = Celery('s3', broker="redis://redis", backend="redis://redis/0")

@app.task
def upload(annex_path, datasetId, tag, public):
    dataset = DataladStore(annex_path).get_dataset(datasetId)

    # create bucket string
    bucket_string = 'ssh://' + os.environ['AWS_S3_TEST_BUCKET']

    # create sibling
    sibling = datalad.api.create_sibling(bucket_string, dataset=dataset)
    return 'result'