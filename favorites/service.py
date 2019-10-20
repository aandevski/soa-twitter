import os
import requests
import functools
from flask import request, jsonify

kong_host = os.environ.get('KONG_HOST')
kong_port = os.environ.get('KONG_PORT')


def check_user_existence(user_id):
    request_url = f"http://{kong_host}:{kong_port}/users/{user_id}"
    reply = requests.get(request_url)
    if reply.status_code != requests.status_codes.codes.ok:
        raise Exception('User with id={} does not exist'.format(user_id))


def check_tweet_existence(tweet_id):
    request_url = f"http://{kong_host}:{kong_port}/tweets/{tweet_id}"
    reply = requests.get(request_url)
    if reply.status_code != requests.status_codes.codes.ok:
        raise Exception(f'Tweet with id={tweet_id} does not exist')


def get_tweet(tweet_id):
    request_url = f"http://{kong_host}:{kong_port}/tweets/{tweet_id}"
    reply = requests.get(request_url)
    return reply.json()


def get_user(user_id):
    request_url = f"http://{kong_host}:{kong_port}/users/{user_id}"
    reply = requests.get(request_url)
    return reply.json()


def user_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if request.headers.get("X-Consumer-Username") is None:
            return jsonify(error='Not logged in'), 401
        user = get_user(request.headers.get("X-Consumer-Username"))
        return view(user, *args, **kwargs)
    return wrapped_view