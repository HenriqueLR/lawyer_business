#!/bin/bash -xe

apt-get install -y sudo && sudo apt-get -y update \
&& ./env/sys/add-user.sh \
&& apt-get install -y postgresql && apt-get install -y postgresql-contrib \
&& ./env/postgresql/configure-postgresql.sh \
&& apt-get install -y nginx \
&& cp ./env/nginx/default /etc/nginx/sites-enabled/default \
&& pip install -r ./requirements.txt \
&& cp ./env/supervisord/supervisord.conf /etc/supervisord.conf \
&& find . -name "*.sqlite3" | xargs rm -f \
&& find . -path "*/migrations/*.py" -not -name "__init__.py" -delete \
&& find . -name "*.pyc" | xargs rm -f \
&& ./app/manage.py collectstatic --noinput \
&& ./app/manage.py makemigrations --settings=conf.settings_production \
&& ./app/manage.py migrate --settings=conf.settings_production \
&& python app/conf/config_init.py --conf production \
&& rm -rf /var/lib/apt/lists/* && apt-get clean
