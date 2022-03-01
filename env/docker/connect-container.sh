#!/bin/bash -xe

argc=$#
argv=($@)

Connect(){
	sudo docker exec -i -t $image /bin/bash
}

image=$1
tag=$2

Connect
