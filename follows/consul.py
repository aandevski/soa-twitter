import consulate
import os

consul = consulate.Consul(host=os.environ['CONSUL_HOST'], port=os.environ['CONSUL_PORT'])


def register():
    host = os.environ['SERVICE_IP']
    port = os.environ['SERVICE_PORT']
    service_name = os.environ['SERVICE_NAME']
    consul.agent.service.register(name=service_name, port=int(port), address=host)
