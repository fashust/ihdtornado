# -*- coding: utf-8 -*- #
"""
    application runner
"""
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_command_line

from application import Application


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


define('host', default='0.0.0.0', type=str, help='server bind host')
define('port', default=8000, type=int, help='server bind port')


def run(host, port):
    """
        run server
        :param host - str, bind host
        :param port - int, bind port
    """
    app = Application()
    http_server = HTTPServer(app)
    http_server.listen(port, address=host)
    IOLoop.instance().start()



if __name__ == '__main__':
    parse_command_line()
    run(options.host, options.port)