#!/bin/sh

cd `dirname $0`
docker-compose build --no-cache
docker-compose up -d
docker-compose exec app bash
