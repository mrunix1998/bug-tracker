#!/bin/bash


docker image build -t bug_tracker .
docker container rm -f bug_tracker
docker container run -d -p 8000:8000 --name bug_tracker --env-file ./vars.env --mount 'type=volume,src=db.sqlite3,dst=/home/user/project_core' bug_tracker


docker image build -t bug_tracker_worker -f CronDockerfile .
docker container rm -f bug_tracker_worker
docker container run -d --name bug_tracker_worker --env-file ./vars.env --mount 'type=volume,src=db.sqlite3,dst=/home/user/project_core' bug_tracker_worker
