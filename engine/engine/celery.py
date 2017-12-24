from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'engine.settings')

app = Celery('engine')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task
def add(x, y):
    return x + y

app.conf.beat_schedule = {
    'add-everyday at 8am and 8pm': {
        'task': 'api.tasks.booking_status_update',
        'schedule': crontab(hour='8,16', minute=0),
        'args': []
    },
}
app.conf.timezone = 'UTC'
