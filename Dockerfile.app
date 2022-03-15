FROM henriquelr89/ubuntu-versions:20.04
MAINTAINER henrique.lr89@gmail.com

RUN mkdir -p /deploy/apps/lawyer_business/
ADD . /deploy/apps/lawyer_business/

WORKDIR /deploy/apps/lawyer_business
RUN ./env/docker/install.sh
COPY ./entrypoint.sh /deploy/apps/lawyer_business

RUN chown -R lawyer_business:lawyer_business /deploy/apps/lawyer_business/

USER lawyer_business

ENTRYPOINT ["sh", "/deploy/apps/lawyer_business/env/app/entrypoint.sh"]
