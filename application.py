import tornado.autoreload
import tornado.ioloop
import tornado.web
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer


def main():

    sockets = tornado.netutil.bind_sockets(9191)
    tornado.process.fork_processes(2)

    from flask_app import app
    import urls

    server = HTTPServer(WSGIContainer(app))
    server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
