#!/bin/bash -xe

argc=$#
argv=($@)

Runserver(){
    Remove;
    docker run -d -i -t -v "$(pwd):/deploy/apps/lawyer_business" -p 0.0.0.0:80:80 -p 0.0.0.0:4444:5432 --name "lawyer_business" "lawyer_business:v.0.1" ./env/services.sh;
}

Remove(){
    docker rm -f lawyer_business || true;
}

Runserver
