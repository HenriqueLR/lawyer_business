#!/bin/bash -xe

sudo -u postgres psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';"
sudo -u postgres psql --command "CREATE DATABASE docker;"
sudo -u postgres psql --command "GRANT ALL PRIVILEGES ON DATABASE docker to docker;"

sudo echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/12/main/pg_hba.conf \
&& echo "listen_addresses='*'" >> /etc/postgresql/12/main/postgresql.conf \
&& /etc/init.d/postgresql restart
