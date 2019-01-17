#!/usr/bin/env python3
# encoding: utf-8
import threading
from time import sleep, time
from common.database import RedisClients,ElasticsClient
from common.utils import get_logger


class MetadataStorage:
    def __init__(self):
        self.ElasticsClients = ElasticsClient(ELASTICS_INDEX_NAME,ELASTICS_INDEX_TYPE,_index_mappings) 
        self.logger = get_logger("logger_metadata_")
    
    def init_index(self):
        self.ElasticsClients.create_index()

    def start(self):
        timer = threading.Timer(5,self.sdf)
        timer.start()

    def sdf(self):
        print(time())


# elastics 索引名
ELASTICS_INDEX_NAME = "test"
    # elastics 索引类型
ELASTICS_INDEX_TYPE = "test_type"
 #创建映射
_index_mappings = {
    "mappings": {
        ELASTICS_INDEX_TYPE: {
            "properties": {
                "info_hash": {
                    "type": "keyword",
                    "index": True
                },
                "bare_name": {
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                },
                "create_time": {
                    "type": "long"
                },
                "update_time": {
                    "type": "long"
                },
                "file_size": {
                    "type": "long"
                },
                "file_num": {
                    "type": "long"
                },
                "file_type": {
                    "type": "long"
                },
                "hot": {
                    "type": "long"
                },
                "file_list":{
                    "type": "text",
                    "index": True,
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                }
            }
        }

    }
}