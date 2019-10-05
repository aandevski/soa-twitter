import os
import requests

KONG_ADDRESS = f"{os.environ['KONG_HOST']}:{os.environ['KONG_PORT']}"


def create_consumer(id):
    request_url = f"http://{KONG_ADDRESS}/consumers/"
    reply = requests.post(request_url, data={
        "username": id
    })
    if reply.status_code != requests.status_codes.codes.created:
        raise Exception('Failed')


def get_token(id):
    request_url = f"http://{KONG_ADDRESS}/consumers/{id}/key-auth"
    reply = requests.post(request_url)
    if reply.status_code != requests.status_codes.codes.created:
        raise Exception('Failed')
    return reply.json()['key']
