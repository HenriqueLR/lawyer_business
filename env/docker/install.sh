#!/bin/bash -xe

sudo echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
&& apt-get -y update \
&& apt-get -y install software-properties-common python-software-properties \
&& add-apt-repository ppa:jonathonf/python-3.6 --yes \
&& apt-get update \
&& apt-get -y install python3.6 \
&& apt-get install -y openssh-server \
&& ./env/sys/add-user.sh \
&& apt-get install -y nginx \
&& cp ./env/nginx/default /etc/nginx/sites-enabled/default \
&& apt-get install -y curl wget \
&& apt-get install -y libpq-dev python-pip python-dev build-essential freetds-dev --force-yes \
&& apt-get install -y libaio1 psmisc libnuma1 libstdc++6 libjpeg-dev \
&& apt-get install -y python-psycopg2 \
&& pip install -r ./requirements.txt \
&& cp ./env/supervisord/supervisord.conf /etc/supervisord.conf \
&& ./env/postgresql/configure-postgresql.sh \
&& find . -name "*.sqlite3" | xargs rm -f \
&& find . -path "*/migrations/*.py" -not -name "__init__.py" -delete \
&& find . -name "*.pyc" | xargs rm -f \
&& ./app/manage.py collectstatic --noinput \
&& ./app/manage.py makemigrations --settings=conf.settings_production \
&& ./app/manage.py migrate --settings=conf.settings_production
