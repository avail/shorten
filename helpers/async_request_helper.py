import tornado
import tornado.web
import tornado.gen
from tornado.ioloop import IOLoop

from multiprocessing.pool import ThreadPool
pool = ThreadPool(4)

class asyncRequestHandler(tornado.web.RequestHandler):
    """
    Tornado asynchronous request handler
    create a class that extends this one (requestHelper.asyncRequestHandler)
    use asyncGet() and asyncPost() instad of get() and post().
    Done. I'm not kidding.
    """
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, *args, **kwargs):
        try:
            yield tornado.gen.Task(runBackground, (self.asyncGet, tuple(args), dict(kwargs)))
        except Exception as e:
            yield tornado.gen.Task(self.captureException, exc_info=True)
        finally:
            if not self._finished:
                self.finish()

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self, *args, **kwargs):
        try:
            yield tornado.gen.Task(runBackground, (self.asyncPost, tuple(args), dict(kwargs)))
        except Exception as e:
            yield tornado.gen.Task(self.captureException, exc_info=True)
        finally:
            if not self._finished:
                self.finish()

    def asyncGet(self, *args, **kwargs):
        self.send_error(405)
        self.finish()

    def asyncPost(self, *args, **kwargs):
        self.send_error(405)
        self.finish()


def runBackground(data, callback):
    """
    Run a function in the background.
    Used to handle multiple requests at the same time
    """
    func, args, kwargs = data
    def _callback(result):
        IOLoop.instance().add_callback(lambda: callback(result))
    pool.apply_async(func, args, kwargs, _callback)