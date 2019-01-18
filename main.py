#!/usr/bin/env python3
# encoding: utf-8
import time, threading
from common.database import RedisClients,ElasticsClient
from metadata_storage import MetadataStorage
import app

if __name__ == "__main__":
  
    me = MetadataStorage("bt_metadata","doc",10000)
    me.init_index()
    t2 = threading.Thread(target=me.start)
    t2.start()

    app = app.create_app()
    t1 = threading.Thread(target=app.run,args=('0.0.0.0',8000))
    t1.start()
