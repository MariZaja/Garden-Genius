#!/bin/bash

docker-compose down

docker image rmi "$(docker images | grep 'postgres-postgres' | awk '{print $3}')"

docker volume rm postgres_pgdata