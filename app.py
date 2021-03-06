# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import options

options.parse_command_line()
from route import routes
from setting import settings
from util.log import logger

logger.init(logpath=options.logpath, log_level=settings['log_level'])


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, routes, **settings)

if __name__ == "__main__":
    # tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
