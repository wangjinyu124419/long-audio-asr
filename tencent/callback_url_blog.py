import time
import  logging
import logging.handlers
import  json
import tornado.ioloop
import tornado.web
import tornado.httpserver


def setup_logging(level=logging.DEBUG, stream=True, stream_level=logging.DEBUG,
                  *, save_file=True, filename=''):
    formatter = logging.Formatter(
        '[%(levelname)1.1s %(asctime)s.%(msecs)03d %(name)s:%(lineno)d] %(message)s',
        datefmt='%y%m%d %H:%M:%S',
    )
    logging.getLogger().setLevel(level)
    if save_file:
        rotating_file_handler = logging.handlers.RotatingFileHandler(
            'server.log' if not filename else filename,
            mode='a',
            maxBytes=100*1024*1024,
            backupCount=10,
            encoding='utf-8',
        )
        rotating_file_handler.setFormatter(formatter)
        logging.getLogger().addHandler(rotating_file_handler)
    if stream:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(stream_level)
        logging.getLogger().addHandler(stream_handler)

setup_logging(filename='server.log')

logger=logging.getLogger(__name__)

class MainHandler(tornado.web.RequestHandler):


    #定义tornado的post方法
    def post(self, *args, **kwargs):
        callback = {}


        try:
            response = self.request.body
            res_dict=json.loads(response.decode('utf-8'))
            text=res_dict['data']['text']
        except Exception as err:
            logger.exception('get_result_fail')
            # logger.debug('get_result_fail %r',err)
            callback['ret'] = -1
            callback['msg'] = err.__repr__()
        else:
            logger.debug('res_dict:%r'%res_dict)

            fp=open('tencent.txt','a')
            fp.write(text+'\n')

            callback['ret']=0
            callback['msg']='ok'



        self.write(callback)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(8322)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()