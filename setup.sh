#!/bin/bash -xe

argc=$#
argv=($@)


bd(){
	: '
	create image postgresql
	'
	sudo docker build -f Dockerfile.bd -t "$image:$tag" .;
}

app(){
	: '
	create image app
	'	
	sudo docker build -f Dockerfile.app -t "$image:$tag" .; 
}

image=$1
tag=$2

$3
