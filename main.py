import tornado.ioloop
import tornado.web
import tornado.gen

from helpers import async_request_helper
from helpers import database_helper
from helpers import misc_helper
from helpers import config_helper
from helpers import log_helper

config = config_helper.Config()
config.load_config()

log = log_helper.Log()

database = database_helper.Database()
database.init(config.get_db_name())

errors = [ "", "Only POST shortening is allowed", "Not a valid URL, you dummy", "WHAT" ]

class HandleRoot(async_request_helper.asyncRequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def asyncGet(self):
        self.render("main.tpl", title = config.get_site_title(), errors = errors, errorid = 0)

class HandleShortening(async_request_helper.asyncRequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def asyncGet(self):
        # json response for api?
        # ajax request on site itself perhaps idfk
        self.render("main.tpl", title = "{} - Error".format(config.get_site_title()), errors = errors, errorid = 1 )

    @tornado.web.asynchronous
    @tornado.gen.engine
    def asyncPost(self):
        try:
            shortened = database.shorten_url(self.get_argument("url"))
            self.write(shortened)
        except Exception as e:
            log.printError(e)
            self.write(str(e))

class HandleInvalidUrl(async_request_helper.asyncRequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def asyncGet(self):
        self.render("main.tpl", title = config.get_site_title(), errors = errors, errorid = 2)

class HandleUrls(async_request_helper.asyncRequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def asyncGet(self, arg):
        log.print("Requested ID {}".format(arg), log.YELLOW)
        try:
            url = database.get_url(arg)
            self.redirect(url)
            clicks = database.add_click(arg)
            log.printSuccess("Redirected {} to {} successfully! Clicks: {}".format(arg, url, clicks))
        except Exception as e:
            log.printError(e)
            self.render("main.tpl", title = "{} - Error".format(config.get_site_title()), errors = errors, errorid = 3 )

def main():
    return tornado.web.Application([
        (r"/", HandleRoot),
        (r"/shorten", HandleShortening),
        (r"/invalid", HandleInvalidUrl),
        (r'/(\w+)', HandleUrls),
        (r'/assets/(.*)', tornado.web.StaticFileHandler, {"path": "assets/"})],
        template_path = "templates/",
        compiled_template_cache = False,
        debug = config.get_debug())

if __name__ == "__main__":

    app = main()
    app.listen(config.get_port())

    tornado.ioloop.IOLoop.current().start()



