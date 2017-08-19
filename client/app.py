from celery import Celery
from flask import Flask, render_template, request


REDIS_URL = 'redis://redis:6379/0'
celery = Celery(broker=REDIS_URL, backend=REDIS_URL)



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = dict(task='tasks.add', val1=1, val2=2)
        result = None
    if request.method == 'POST':
        form = request.form
        task = form['task']
        val1 = int(form['val1'])
        val2 = int(form['val2'])
        result = celery.signature(task).apply_async((val1, val2,)).get()
    return render_template('index.html', form=form, result=result)

