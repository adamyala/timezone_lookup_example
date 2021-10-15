FROM python:3.9

# runs the mkdir command within the container because we need a place to put the code
RUN mkdir /var/www
# set the working directory to our code directory. if not, we'll end up copying code to /
WORKDIR /var/www
# adds files from our laptop to the containers code directory
ADD . /var/www

# install postgresql-client so wait-for-postgres.sh can run in this container
RUN apt-get update && \
    apt install -y postgresql-client && \
    pip install -r requirements.txt
