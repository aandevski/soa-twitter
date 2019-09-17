import os
import requests

KONG_ADDRESS = f"{os.environ['KONG_HOST']}:{os.environ['KONG_PORT']}"


def create_consumer(username):
    request_url = f"http://{KONG_ADDRESS}/consumers/"
    reply = requests.post(request_url, data={
        "username": username
    })
    if reply.status_code != requests.status_codes.codes.created:
        raise Exception('Failed')


def get_token(username):
    request_url = f"http://{KONG_ADDRESS}/consumers/{username}/key-auth"
    reply = requests.post(request_url)
    if reply.status_code != requests.status_codes.codes.created:
        raise Exception('Failed')
    return reply.json()['key']
