FROM henriquelr89/ubuntu-versions:14.04
MAINTAINER henrique.lr89@gmail.com

RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf
RUN locale-gen en_US.UTF-8

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir -p /deploy/apps/lawyer_business/
ADD . /deploy/apps/lawyer_business/

WORKDIR /deploy/apps/lawyer_business
RUN ./env/docker/install.sh

USER lawyer_business