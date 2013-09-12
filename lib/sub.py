import sys
if 'gevent' in sys.modules:
    import zmq.green as zmq
else:
    import zmq
try:
    import ujson as json
except ImportError:
    import json    

class Subscriber(object):

    def __init__(self, connect="tcp://127.0.0.1:1234", context=None, chan="h"):

        if context is None:
            self.context = zmq.Context()
        else:
            self.context = context

        self.socket = self.context.socket(zmq.SUB)
        self.socket.setsockopt(zmq.SUBSCRIBE, chan)
        self.socket.connect(connect)
        self.socket.setsockopt(zmq.SNDHWM, 1)
        self.socket.setsockopt(zmq.RCVHWM, 1)

    def get(self, decode=True):
        msg = self.socket.recv_multipart()[1]

        if not decode:
            return msg
            
        return json.loads(msg)
