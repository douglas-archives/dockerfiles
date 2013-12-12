# Django - gunicorn + nginx (reverse proxy)
#
# VERSION       1.0

# more info about douglasmiranda/python-base:
# https://index.docker.io/u/douglasmiranda/python-base/
# https://github.com/douglasmiranda/dockerfiles/tree/master/python-base
FROM douglasmiranda/python-base
# FROM douglasmiranda/gnginx-tmp

MAINTAINER Douglas Miranda douglasmirandasilva@gmail.com

# for Pillow
RUN apt-get -y install libjpeg8-dev
# if you want support for all things:
# RUN apt-get -y install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev

# for gevent - worker_class for gunicorn
RUN apt-get -y install libevent-dev

# supervisor - for monitoring
RUN apt-get install -y supervisor

# The compact version of the Vim
RUN apt-get install -y vim-tiny

# Nginx
RUN apt-get install -y nginx

ADD etc/ /etc/
RUN mkdir /opt/run/
ADD bin/run_app_server /opt/run/
RUN chmod +x opt/run/run_app_server

VOLUME ["/webapps"]
VOLUME ["/logs"]

# Launch the programs
# ENTRYPOINT ["/opt/run/run_app_server"]
# CMD ["/usr/bin/supervisord", "-n"]