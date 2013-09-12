#!/usr/bin/env python
import lib.sub
import argparse
import time
try:
    import ujson as json
except ImportError:
    import json

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Headset client")
    parser.add_argument("-a", action="store", type=str, default="tcp://127.0.0.1:1234", help="Connect to address")
    parser.add_argument("-c", action="store", type=str, default="h", help="Subscribe to channel")
    parser.add_argument("-r", action="store", type=str, default=False, help="Record to file")
    args = parser.parse_args()

    client = lib.sub.Subscriber(**{
        "connect": args.a,
        "chan": args.c
    })

    if args.r:
        f = open(args.r, "w")
        try:
            while True:
                msg = client.get(decode=False)
                line = ":".join(( "{0:.5f}".format(time.time()), msg))
                f.write(line+"\n")
        except KeyboardInterrupt:
            f.close()

    else:
        while True:
            print(client.get())
