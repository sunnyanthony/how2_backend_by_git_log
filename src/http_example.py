from http import server
from urllib import parse
import signal, os
import logging

logging.basicConfig(filename='/data/socket_server.log', encoding='utf-8', level=logging.DEBUG)

def signal_handler(sig, frame):
    print(f'game over {sig} {frame}')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class MyHandler(server.BaseHTTPRequestHandler):
    def _predefine(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _body(self, text: str):
        # write body
        self.wfile.write(text.encode())

    def do_GET(self):
        copy_path = self.path
        logging.info(f"request: {copy_path}")
        url = parse.urlparse(copy_path)
        if url.path == '/test':
            self._predefine()
            self._body("hi")
            self.dict = parse.parse_qs(url.query)
            logging.info(f'get {self.dict}')
        else:
            self.send_error(404,'File Not Found: %s' % self.path)

class Server(object):
    def __init__(self, host = "", port = 8080, Handler = server.BaseHTTPRequestHandler):
        self.host = host
        self.port = port
        self.server_bind = server.HTTPServer
        self.hander = Handler
        self.http = None

    def run(self):
        self.http = self.server_bind((self.host, self.port), self.hander)
        self.http.serve_forever()

    def send(self, ):
        pass #self.request()

s = Server(port = 1234, Handler = MyHandler)
try:
    s.run()
except Exception as e:
    logging.exception(f'{e}')
logging.info('abort')
