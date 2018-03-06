#!/bin/bash -xe

sudo apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3 --force-yes \
&& /etc/init.d/postgresql start

sudo -u postgres psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';"
sudo -u postgres psql --command "CREATE DATABASE docker;"
sudo -u postgres psql --command "GRANT ALL PRIVILEGES ON DATABASE docker to docker;"

sudo echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf \
&& echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf \
&& /etc/init.d/postgresql restart
