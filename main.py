#!/usr/bin/env python3
# encoding: utf-8

import argparse
import time, threading
from common.database import RedisClients,ElasticsClient
from metadata_storage import MetadataStorage
import app

def get_parser():
    parser = argparse.ArgumentParser(description="start main.py with flag.")
    parser.add_argument(
        "-w", action="store_true", help="run web_server func."
    )
    parser.add_argument(
        "-m", action="store_true", help="run metadata_storage_task func"
    )

    parser.add_argument(
        "-a", action="store_true", help="run web_server & metadata_storage_task func"
    )

    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    global app
    if args["w"]:
        app = app.create_app()
        t1 = threading.Thread(target=app.run,args=('0.0.0.0',8000))
        t1.start()
    elif args["m"]:
        me = MetadataStorage(2)
        me.init_index()
        t2 = threading.Thread(target=me.start)
        t2.start()
    elif args["a"]:
        me = MetadataStorage(2)
        me.init_index()
        t2 = threading.Thread(target=me.start)
        t2.start()

        apps = app.create_app()
        t1 = threading.Thread(target=apps.run,args=('0.0.0.0',8000))
        t1.start()

if __name__ == "__main__":
    command_line_runner()
    

    
