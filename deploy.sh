#!/bin/bash


docker image build -t backend .
docker container rm -f backend
docker container run -d -p 8000:8000 --name backend backend


docker image build -t worker -f CronDockerfile .
docker container rm -f worker
docker container run -d --name worker worker
