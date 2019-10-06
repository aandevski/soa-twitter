import os
import consul
import requests

users_service = os.environ['USERS_SERVICE_NAME']


def check_user_existence(user_id):
    service_data = consul.get_value(users_service)
    host = service_data.get('host')
    port = service_data.get('port')
    request_url = f"http://{host}:{port}/{user_id}"
    reply = requests.get(request_url)
    if reply.status_code != requests.status_codes.codes.ok:
        raise Exception('User with id={} does not exist'.format(user_id))
