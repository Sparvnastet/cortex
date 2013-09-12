#!/usr/bin/env python2
import lib.pub
import argparse
import logging
import sys
import decimal
import time

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Headset server")
    parser.add_argument("-b", action="store", type=str, default="tcp://127.0.0.1:1234", help="Bind to address")
    parser.add_argument("-c", action="store", type=str, default="h", help="Publish to channel")
    parser.add_argument('-r', dest='record', action='store_true', help="Read recording from stdin")
    parser.add_argument('--nodebug', dest='debug', action='store_false')
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    if args.record:
        last = None
        server = lib.pub.Publisher(**{
            "bind": args.b,
            "chan": args.c
        })
        
        for line in sys.stdin:
            tstamp, line = line.rstrip("\n").split(":", 1)
            tstamp = float(decimal.Decimal(tstamp))

            if last is not None:
                time.sleep(tstamp-last)
            server.put(line)
            last = tstamp

    else:
        server = lib.pub.HeadsetRelay(**{
            "bind": args.b,
            "chan": args.c
        })
        server.run()
