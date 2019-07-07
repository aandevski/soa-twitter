#!/bin/sh

curl -i -X POST \
  --url http://$1/services/ \
  --data 'name=tweets' \
  --data 'url=http://tweets.service.consul'

curl -i -X POST \
  --url http://$1/services/tweets/routes \
  --data 'paths[]=/tweets'

curl -i -X POST \
  --url http://$1/services/ \
  --data 'name=users' \
  --data 'url=http://users.service.consul'

curl -i -X POST \
  --url http://$1/services/users/routes \
  --data 'paths[]=/users'

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