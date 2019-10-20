import os
import requests

kong_host = os.environ.get('KONG_HOST')
kong_port = os.environ.get('KONG_PORT')


def check_user_existence(user_id):
    request_url = f"http://{kong_host}:{kong_port}/users/{user_id}"
    reply = requests.get(request_url)
    if reply.status_code != requests.status_codes.codes.ok:
        raise Exception('User with id={} does not exist'.format(user_id))
