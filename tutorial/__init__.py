from pyramid.config import Configurator
from pyramid.response import Response

import ptvsd


def hello_world(request):
    #print (x)
    return Response('<body><h1>Hello World!</h1></body>')


def main(global_config, **settings):
    print("start...")
    address = ('0.0.0.0', 3000)
    ptvsd.enable_attach(address)
    ptvsd.wait_for_attach()

    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')

    return config.make_wsgi_app()
