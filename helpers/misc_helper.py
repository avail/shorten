import uuid

from helpers import log_helper

log = log_helper.Log()

def rand_id(strlen = 5):
    random = str(uuid.uuid4())
    random = random.replace("-","")
    return random[0:strlen]

def print_arguments(thing):
    msg = "[ARGS] "
    for i in thing.request.arguments:
        msg += "{} = {}\r\n".format(i, thing.get_argument(i))
    log.print(msg, log.YELLOW)
