from __future__ import absolute_import,unicode_literals
import os, sys
from celery import Celery


# from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# _set_current_app(app)
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../myproject')))
# django.setup()
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


