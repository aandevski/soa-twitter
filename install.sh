#!/bin/sh

# configrued at 127.0.0.1:8100


curl -i -X POST \
  --url http://$1/services/ \
  --data 'name=tweets' \
  --data 'url=http://tweets.service.consul'
curl -i -X POST \
  --url http://$1/services/tweets/routes \
  --data 'paths[]=/tweets'
curl -X POST http://$1/services/tweets/plugins \
  --data "name=key-auth"


curl -i -X POST \
  --url http://$1/services/ \
  --data 'name=users' \
  --data 'url=http://users.service.consul'
curl -i -X POST \
  --url http://$1/services/users/routes \
  --data 'paths[]=/users'
curl -X POST http://$1/services/users/plugins \
  --data "name=key-auth"


curl -i -X POST \
  --url http://$1/services/ \
  --data 'name=follows' \
  --data 'url=http://follows.service.consul'
curl -i -X POST \
  --url http://$1/services/follows/routes \
  --data 'paths[]=/follows'


curl -i -X POST \
  --url http://$1/services/ \
  --data 'name=favorites' \
  --data 'url=http://favorites.service.consul'
curl -i -X POST \
  --url http://$1/services/favorites/routes \
  --data 'paths[]=/favorites'