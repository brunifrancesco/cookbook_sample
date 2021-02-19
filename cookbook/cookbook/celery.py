import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cookbook.settings')

app = Celery('cookbook')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)

from celery.schedules import crontab

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'cookbook.celery.debug_task',
        'schedule': crontab(hour=19, minute=4),
        'args': ("Scheduled task",),
    },
}

@app.task(bind=True)
def debug_task(self, param):
    print(f'Request: {self.request!r}')
    print(param)