#!/usr/bin/env python3
# encoding: utf-8
import threading
from time import sleep, time
from common.database import RedisClients,ElasticsClient
from common.utils import get_logger

class MetadataStorage:
    def __init__(self,index_name,index_type,task_time):
        self.ElasticsClients = ElasticsClient(index_name,index_type) 
        self.task_time = task_time
        self.logger = get_logger("logger_metadata_")
        
    def init_index(self):
        self.ElasticsClients.create_index(_index_mappings)

    def start(self):
        self.task_handle()
        timer = threading.Timer(self.task_time,self.start)
        timer.start()

    def task_handle(self):
        # keys = RedisClients.getKeys()
        # for key in keys:
        #     print(str(key,encoding='utf-8'))
        self.logger.info("种子入库任务开始 >>>> {0} !".format(time()))
        value = RedisClients.getValue('db1bfeb897d49b4f98fafa6e0c23a6b9734780a2')
        v = eval(value)
        list = [
            {   "info_hash": v['info_hash'],
                "bare_name": v['bare_name'],
                "create_time": v['create_time'],
                "update_time": v['update_time'],
                "file_size": v['file_size'],
                "file_num": v['file_num'],
                "file_type": v['file_type'],
                "hot": v['hot'],
                "file_list": str(v['file_list']),
                "status": v['status'],
             }
        ]
        self.ElasticsClients.Index_Data(list,v['info_hash'])



# elastics 索引类型
ELASTICS_INDEX_TYPE = "doc"
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
                },
                "status": {
                    "type": "keyword",
                    "index": True
                },
            }
        }

    }
}