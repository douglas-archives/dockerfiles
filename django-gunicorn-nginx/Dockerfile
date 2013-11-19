# Django - gunicorn + nginx (reverse proxy)
#
# VERSION       1.0

# more info about douglasmiranda/python-base:
# https://index.docker.io/u/douglasmiranda/python-base/
# https://github.com/douglasmiranda/dockerfiles/tree/master/python-base
FROM douglasmiranda/python-base

MAINTAINER Douglas Miranda douglasmirandasilva@gmail.com

# for Pillow
RUN apt-get -y install libjpeg8-dev
# if you want support for all things:
# RUN apt-get -y install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev

# for gevent
RUN apt-get -y install libevent-dev

# Nginx
RUN apt-get install -y nginx
# With this
RUN cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup
RUN rm /etc/nginx/nginx.conf
ADD etc/ /django_apps/etc/
RUN ln -s /django_apps/etc/nginx/nginx.conf /etc/nginx/nginx.conf
RUN service nginx restart

# The compact version of the Vim
RUN apt-get install -y vim-tiny

VOLUME ["/django_apps"]

# Launch the something when launching the container
# ENTRYPOINT ["some-program"]

# run "some-program" as the daemon user
# USER daemon
