#!/bin/bash -xe

groupadd supersudo && echo "%supersudo ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/supersudo
adduser --disabled-password --gecos lawyer_business lawyer_business && usermod -a -G supersudo lawyer_business && mkdir -p /home/lawyer_business/.ssh
echo -e "Host github.com\n\tStrictHostKeyChecking no\n" > /home/lawyer_business/.ssh/config
sudo chown -R lawyer_business:lawyer_business /home/lawyer_business
sudo chmod 600 /home/lawyer_business/.ssh/*