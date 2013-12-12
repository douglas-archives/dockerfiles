import os

bind = '0.0.0.0:8000'
workers = 3
worker_class = 'gevent'
print os.environ.get('SETTINGS_FLAVOR')
print 'blah'
# pidfile = '/webapps//gunicorn.pid'
# django_settings = 'douglasmiranda.settings.prod'
