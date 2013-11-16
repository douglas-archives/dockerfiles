# Django
#
# VERSION       1.0

# more info about douglasmiranda/python-base:
# https://index.docker.io/u/douglasmiranda/python-base/
# https://github.com/douglasmiranda/dockerfiles/tree/master/python-base
FROM douglasmiranda/python-base

MAINTAINER Douglas Miranda douglasmirandasilva@gmail.com

# for gevent
RUN apt-get -y install libevent-dev

# for Pillow
RUN apt-get -y install libjpeg8-dev
# if you want support for all things:
# RUN apt-get -y install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev


VOLUME ["/django_apps"]

# Launch the something when launching the container
# ENTRYPOINT ["some-program"]

# run "some-program" as the daemon user
# USER daemon

# if your(s) django app(s) run on different port(s), just add here.
EXPOSE 8000