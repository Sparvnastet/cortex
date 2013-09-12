import gevent
from emokit import emotiv
import zmq.green as zmq
try:
    import ujson as json
except ImportError:
    import json
import logging

logger = logging.getLogger(__name__)

class Publisher(object):

    def __init__(self, bind="tcp://127.0.0.1:1234", context=None, chan="h"):

        if context is None:
            self.context = zmq.Context()
        else:
            self.context = context

        self.socket = self.context.socket(zmq.PUB)
        self.socket.setsockopt(zmq.SNDHWM, 1)
        self.socket.setsockopt(zmq.RCVHWM, 1)
        self.socket.bind(bind)

        self.chan = chan

    def put(self, packet):
        self.socket.send_multipart([self.chan, packet])


class HeadsetRelay(Publisher):

    def __init__(self, **kwargs):

        super(HeadsetRelay, self).__init__(**kwargs)

        self.headset = emotiv.Emotiv()
        gevent.spawn(self.headset.setup)
        gevent.sleep(1)

    def run(self):
        try:
            while True:
                p = self.headset.dequeue()

                packet = p.sensors
                packet["bat"] = p.battery
                logger.debug(packet)
                self.put(json.dumps(packet))
        finally:
            self.headset.close()
