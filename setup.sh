#!/bin/bash -xe

argc=$#
argv=($@)


setup(){
	sudo docker build -t "$image:$tag" .;
}

image=$1
tag=$2

setup
