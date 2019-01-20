#!/usr/bin/env python3
# encoding: utf-8
import threading
from time import sleep, time
from common.database import RedisClients,RedisClients1,ElasticsClients
from common.utils import get_logger

class MetadataStorage:
    def __init__(self,task_time):
        self.task_time = task_time
        self.logger = get_logger("logger_metadata_")
        
    def init_index(self):
        ElasticsClients.create_index(_index_mappings)

    def start(self):
        self.task_handle()
        timer = threading.Timer(self.task_time,self.start)
        timer.start()

    def task_handle(self):
        try:
            keys = RedisClients.getKeys()
            self.logger.info("种子入库任务开始 >>>> {0}-{1}!".format(time(),len(keys)))
            for key in keys:
                value = RedisClients.getValue(str(key,encoding='utf-8'))
                RedisClients1.set_keyinfo(str(key,encoding='utf-8'),value)
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
                ElasticsClients.Index_Data(list,v['info_hash'])
                RedisClients.deleteByKey(str(key,encoding='utf-8'))
            self.logger.info("种子入库任务完成 >>>> {0}-{1}!".format(time(),len(keys)))
        except Exception as e:
            self.logger.error("种子入库异常 >>>> {0}!".format(e))


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