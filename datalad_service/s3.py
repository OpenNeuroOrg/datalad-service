from kombu import Exchange, Queue
from celery import Celery

app = Celery('hello', broker='redis:6379', backend='redis:6379/celery')


@app.task
def export(datasetId, tag, public):
    queueId = 'dataset'
    queues = app.control.inspect().active_queues()
    return queues
    
    
def create_consumer(queueId):
    return