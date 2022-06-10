#!/bin/bash -xe

./app/manage.py collectstatic --noinput

sudo cp ./env/nginx/default /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/postgresql restart

sudo cp ./env/supervisord/supervisord.conf /etc/supervisord.conf
sudo supervisord -c /etc/supervisord.conf
sudo supervisorctl restart all
/bin/bash
