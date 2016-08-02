import json

class Config():
    data = ""

    def load_config(self):
        with open('config.json') as cfg_file:
            self.data = json.load(cfg_file)

    def get_port(self):
        return self.data["port"]

    def get_site_title(self):
        return self.data["site-title"]

    def get_debug(self):
        debug = self.data["debug"]
        if debug is not "true":
            return False
        else:
            return True

    def get_db_name(self):
        return self.data["database"]