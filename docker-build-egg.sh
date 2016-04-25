#!/bin/bash
set -x
docker build -t $USER/coronado-eventmanagerplugin .
mkdir -p dist
docker run --rm \
    -e USERID=$EUID \
    -v `pwd`/dist:/root/EventManagerPlugin/dist \
    $USER/coronado-eventmanagerplugin
