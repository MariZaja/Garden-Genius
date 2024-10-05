#!/bin/bash

docker-compose down

docker image rmi "$(docker images | grep 'db-postgres' | awk '{print $3}')"

docker volume rm db_pgdata