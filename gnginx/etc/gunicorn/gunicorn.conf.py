import os

ENV = os.environ
bind = '0.0.0.0:8000'
workers = 3
worker_class = 'gevent'
# you can use the env vars, example:
# pidfile = '/webapps/{0}/gunicorn.pid'.format(ENV.get('DJANGO_PROJECT_NAME'))
# django_settings = '{0}.settings.prod'.format(ENV.get('DJANGO_PROJECT_NAME'))
