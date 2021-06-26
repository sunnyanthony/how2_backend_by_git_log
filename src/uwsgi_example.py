import logging
logging.basicConfig(filename='/data/socket_server.log', encoding='utf-8', level=logging.DEBUG)

# class defined
class Hello(object):
    def __init__(self):
        self.callbacks = {}
        self.condition = {}

    # hook the 
    def hook(self, *args):
        logging.info(f"{args}")
        def decorator(f):
            if len(args) >= 1:
                self.callbacks[args[0]] = f
            if len(args) >= 2:
                self.condition[args[0]] = list(args[1:])
            return f
        return decorator

    def find_callback(self, path, con: str):
        logging.info(f"{self.callbacks=}")
        condition_list = self.condition.get(path, [])
        logging.info(f"{condition_list=}")
        if con in condition_list or len(condition_list) == 0:
            return self.callbacks.get(path, None)
        return None
# class defined end

app = Hello()

@app.hook("/")
def root(evn, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello Word"

@app.hook("/test", "GET")
def test(evn, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "hi"

def application(env, start_response):
    logging.info(f'get response {env}')
    ret_str = "We're OK..."
    try:
        method = env.get("REQUEST_METHOD")
        path = env.get("PATH_INFO")
        if path:
            global app
            cb = app.find_callback(path, method)
            if cb:
                ret_str = cb(env, start_response)
        else:
            ret_str = "Not Found"
    except Exception as e:
        start_response('200 OK', [('Content-Type','text/html')])
        ret_str = f'{ret_str} but {e}'
    return [ret_str.encode('ascii')]
