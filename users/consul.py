import sys
import consulate


def register():
    consul = consulate.Consul(host='consul', port=8500)

    for i, arg in enumerate(sys.argv):
        if arg == '-b':
            port = int(sys.argv[i+1][1:])
            consul.agent.service.register(name='users', port=port)
