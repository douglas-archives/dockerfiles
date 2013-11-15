# Python
#
# VERSION       1.0

# use the ubuntu base image provided by dotCloud
FROM ubuntu:12.04

MAINTAINER Douglas Miranda douglasmirandasilva@gmail.com

# make sure the package repository is up to date
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get -y update

# Set up lang
RUN apt-get install -y language-pack-en

ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

# install essential stuff
RUN apt-get install -y openssh-server git-core libxml2-dev curl build-essential make gcc wget libsqlite3-dev sqlite3 libpq-dev

RUN apt-get install -y python python-dev

RUN apt-get install -y python-pip
RUN apt-get install -y python-virtualenv

VOLUME ["/.virtualenvs"]