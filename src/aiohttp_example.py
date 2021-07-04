# refer from https://docs.aiohttp.org/en/stable/web_advanced.html
from aiohttp import web
import logging
logging.basicConfig(filename='/data/aiohttp_server.log', encoding='utf-8', level=logging.DEBUG)

'''
decorator adds routes
routes = web.RouteTableDef()

@routes.get('/')
async def root(req):
    return web.Response(text="Hello Word")

@routes.view("/test")
class test(web.View):
    async def get(self):
    	return web.Response(text="hi geter")

    async def post(self):
    	return web.Response(text="hi geter")

app = web.Application()
app.add_routes(routes)
'''
class Handler:
    def __init__(self, app):
        import inspect
        #register handlers by function name
        # default is get
        self.handlers = [web.get('/' + attr, getattr(self, attr)) for attr in dir(self) if inspect.ismethod(getattr(self, attr)) \
                         and not attr.startswith('_') and not attr.startswith('post_') and attr != 'root']
        # root path
        self.handlers.append(web.get('/', self.root))
        # post requests
        self.handlers.extend([web.get('/' + attr[5:], getattr(self, attr)) for attr in dir(self) if inspect.ismethod(getattr(self, attr)) \
                         and not attr.startswith('_') and attr.startswith('post_') and attr != 'root'])
        self.app = app
        app.add_routes(self.handlers)

    async def root(self, req):
    	logging.info('root')
    	return web.Response(text="Hello Word")

    async def test(self, req):
    	logging.info('test')
    	return web.Response(text="hi geter")

    async def post_test(self, req):
    	return web.Response(text="hi poster")

    async def _start(self, app):
        logging.info("preparing message queue, cache, db etc.")

    async def _end(self, app):
        logging.info("cleaning message queue, cache, db etc.")

async def start():
    logging.info(f'start')
    try :
        app = web.Application()
        handlers = Handler(app)
    
        app.on_startup.append(handlers._start)
        app.on_cleanup.append(handlers._end)
    
    except Exception as e:
        logging.exception(f'get exception: {e}')
    finally:
        return app

if __name__ == '__main__':
    # run
    web.run_app(start())