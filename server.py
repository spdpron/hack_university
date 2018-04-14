 #coding:utf8
import json
import sys
import tornado.ioloop
from tornado_json.application import Application
from tornado_json.routes import get_routes
from datetime import datetime

def main():
    import api
    routes = get_routes(api)
    print("we start working at "+str(datetime.now())+"\n\nLink for API: http://localhost:8888/"+str(routes[0][0]))
    application = Application(routes=routes, settings={}, generate_docs=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
