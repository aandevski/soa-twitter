#!/bin/sh

PLUGINREPLY=`curl -X POST http://$1/plugins --data "name=key-auth"`
ANONREPLY=`curl -d "custom_id=anonymous" http://$1/consumers/`

PLUGINID=`echo $PLUGINREPLY | sed 's/.*"id":"\([^"]*\)".*/\1/'`
ANONID=`echo $ANONREPLY | sed 's/.*"id":"\([^"]*\)".*/\1/'`
curl --request PATCH http://$1/plugins/$PLUGINID \
  --data "config.anonymous=$ANONID"


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