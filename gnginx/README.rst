Python Apps with gunicorn + nginx (reverse proxy)
=================================================

(Experimental)

This is optimized for dev environment, but I'm trying to make very easy to switch from dev to production.

I'm assuming you don't need `sudo` to execute your docker commands. `More info <http://docs.docker.io/en/latest/use/basics/#sudo-and-the-docker-group>`_.

I can't assure that won't break if you try for now. I'm always trying something new with these files, but if you want to try, just create a directory `.docker` in your django project (root folder), for example, and put these files in. You may want to have a look in `bin/docker_start_dev` and `Dockerfile` to see if you have all the needed directories and stuff to run.
