#!/bin/bash -xe

apt-get install -y sudo && sudo apt-get -y update \
&& ./env/sys/add-user.sh \
&& apt-get install -y netcat \
&& pip install -r ./requirements.txt \
&& mkdir /etc/supervisord/ && cp ./env/supervisord/supervisord.conf /etc/supervisord/supervisord.conf \
&& rm -rf /var/lib/apt/lists/* && apt-get clean
