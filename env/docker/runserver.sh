#!/bin/bash -xe

argc=$#
argv=($@)

bd(){
    path_pg_data_docker="/var/lib/postgresql/12/main";
    volume_local_pg_data="pg-data";
    ip_port_bd=0.0.0.0:5432:5432;
    service=bd;
    remove;
    docker run -d -i -t -v "$volume_local_pg_data:$path_pg_data_docker" -p $ip_port_bd --env-file ./.envdb --name "$image" "$image:$tag" ./env/docker/services.sh $service;
}

app(){
    path_app_docker="/deploy/apps/lawyer_business";
    ip_port_app=0.0.0.0:80:80;
    service=app;
    remove;
    docker run -d -i -t -v "$(pwd):$path_app_docker" -p $ip_port_app --link $parent:db --env-file ./.env --name "$image" "$image:$tag" ./env/docker/services.sh $service;
}

remove(){
    docker rm -f $image || true;
}

image=$1
tag=$2
parent=$4

$3
