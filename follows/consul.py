import consulate
import os


def register():
    consul = consulate.Consul(host=os.environ['CONSUL_HOST'], port=os.environ['CONSUL_PORT'])
    consul.agent.service.register(name='follows', port=int(os.environ['SERVICE_PORT']), address=os.environ['SERVICE_IP'])
