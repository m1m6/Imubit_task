#!/usr/bin/env bash

docker-compose stop
docker-compose rm -vfs

docker-compose up -d --build --force-recreate