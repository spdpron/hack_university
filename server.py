 #coding:utf8
import json
import sys
import tornado.ioloop
from tornado_json.application import Application
from tornado_json.routes import get_routes
from datetime import datetime
from tornado.web import RequestHandler, asynchronous
from tornado import gen
from engine import Engine
from tornado.escape import json_encode
from datetime import datetime
import time

class EngineReciever(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type")

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

    @asynchronous
    def post(self):
        print('start')
        data = json.loads(self.request.body.decode('utf-8'))
        if data["hoursToCrawl"] or data["minutesToCrawl"]:
            s = str(data["hoursToCrawl"])+':'+str(data["minutesToCrawl"])
            d = datetime.strptime(s, "%H:%M")
            time_to_kill = time.mktime(d.timetuple())
            self.engine = Engine(data)
            self.engine.start()
            self.engine.join(time_to_kill)
            self.engine.stop()
        else:
            self.engine = Engine(data)
            self.engine.start()
        self.finish()

def main():
    print("We start working at "+str(datetime.now()))
    application = Application([tornado.web.url(r"/api/bloodbitapi/?", EngineReciever)], settings={})
    http_server = tornado.httpserver.HTTPServer(application, idle_connection_timeout=300)
    http_server.bind(8888)
    http_server.start()
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
