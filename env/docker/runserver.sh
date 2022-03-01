#!/bin/bash -xe

argc=$#
argv=($@)

Runserver(){
    Remove;
    docker run -d -i -t -v "$(pwd):/deploy/apps/lawyer_business" -v "pg-data:/var/lib/postgresql/12/main" -p 0.0.0.0:80:80 -p 0.0.0.0:4444:5432 --name "$image" "$image:$tag" ./env/docker/services.sh;
}

Remove(){
    docker rm -f $image || true;
}

image=$1
tag=$2

Runserver
