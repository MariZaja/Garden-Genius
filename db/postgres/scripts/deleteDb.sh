#!/bin/bash

docker-compose down

docker image rmi "$(docker images | grep 'inynierka-postgres' | awk '{print $3}'
f5ab3496885c)"

docker volume rm inynierka_pgdata