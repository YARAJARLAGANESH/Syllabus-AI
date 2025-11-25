import time, json
def log_info(msg: str, meta: dict=None):
    entry = {'ts': time.time(), 'level':'INFO', 'msg': msg, 'meta': meta}
    print(json.dumps(entry))

def log_error(msg: str, meta: dict=None):
    entry = {'ts': time.time(), 'level':'ERROR', 'msg': msg, 'meta': meta}
    print(json.dumps(entry))
