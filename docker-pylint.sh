#!/bin/bash
set -x
docker build -t $USER/coronado-eventmanagerplugin .
docker run --rm --entrypoint=pylint $USER/coronado-eventmanagerplugin EventManagerPlugin
