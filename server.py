#coding:utf8
import json
import sys
import tornado.ioloop
from tornado_json.application import Application
from tornado_json.routes import get_routes

def main():
    import api
    routes = get_routes(api)
    print("Routes\n======\n\n" + json.dumps(
        [(url, repr(rh)) for url, rh in routes],
        indent=2)
    )
    application = Application(routes=routes, settings={}, generate_docs=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
