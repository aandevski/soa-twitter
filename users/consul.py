import sys
import consulate
import os


def register():
    consul = consulate.Consul(host=os.environ['CONSUL_HOST'], port=os.environ['CONSUL_PORT'])

    for i, arg in enumerate(sys.argv):
        if arg == '-b':
            port = int(sys.argv[i+1][1:])
            consul.agent.service.register(name='users', port=port)
