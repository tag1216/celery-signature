from celery import Celery

REDIS_URL = 'redis://redis:6379/0'
app = Celery(broker=REDIS_URL, backend=REDIS_URL)

@app.task
def add(x, y):
    return x + y

