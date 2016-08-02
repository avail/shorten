from couchdb import Server

from helpers import log_helper
from helpers import misc_helper


log = log_helper.Log()

class Database():
    server = Server("http://localhost:5984")
    database = ""

    def init(self, db):
        self.create_database(db)
        #self.add_example_entry()

    def add_example_entry(self):
        self.database["1233"] = dict(url = "https://getrektby.us", clicks = 0)

    # create database (initial launch)
    def create_database(self, db):
        log.print("Trying to create database \"{}\".".format(db), log.YELLOW)
        try:
            self.database = self.server.create(db)
        except:
            self.database = self.server[db]
            log.print("Database already exists - neat.", log.BLUE)

    # delete the couchdb database
    def delete_database(self):
        log.print("Deleting database.", log.BLUE)
        del self.database

    def shorten_url(self, url):
        if "http" in url:
            rid = misc_helper.rand_id()
            log.print("Trying to shorten {}".format(rid), log.YELLOW)
            try:
                self.database[rid] = dict(url = url, clicks = 0)
                log.printSuccess("Shortened {} to {} successfully!".format(url, rid))
            except Exception as e:
                log.printError("Failed to shorten {} - {}".format(rid, e))

            return rid
        else:
            log.printError("Nice url, yo")

    def add_click(self, rid):
        doc = self.database[rid]
        doc["clicks"] = doc["clicks"] + 1

        self.database[rid] = doc

        return self.database[rid]["clicks"]

    def does_url_exist(self, url):
        # TODO: re-use same IDs for duplicate urls
        log.print("NOT IMPL", log.PINK)

# TODO: Implement this after a registration system.. or api..?
#    def get_clicks(self, id):

    def get_url(self, rid):
        return self.database[rid]["url"]