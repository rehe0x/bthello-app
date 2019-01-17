#!/usr/bin/env python3
# encoding: utf-8

from common.database import RedisClients,ElasticsClient
from metadata_storage import MetadataStorage

if __name__ == "__main__":
    # keys = RedisClients.getKeys()
    # for key in keys:
    #     print(str(key,encoding='utf-8'))

    # value = RedisClients.getValue('db1bfeb897d49b4f98fafa6e0c23a6b9734780a2')
    # v = eval(value)
    # print(v)
    # print(v['bare_name'])
    # list = [
    #         {   "info_hash": "345345",
    #             "bare_name": "测试",
    #             "create_time": 12312313,
    #             "update_time": 123123,
    #             "file_size": 1,
    #             "file_num": 1,
    #             "file_type": 1,
    #             "hot": 1,
    #             "file_list": "[{'n':  'Allegra - Woodman Casting X (2016).mp4','l':  938678544}]",
    #          }
    #           ]

    # ElasticsClients.Index_Data(list,'008158817c82b774b61f807fef71bc1bc0587bf4')
    # S = ElasticsClient("bt_metadata","doc")

    # S.Get_Data_By_Body()
    # ElasticsClients.delete_index('test')
    # print(2)
    me = MetadataStorage("bt_metadata","doc",100)
    me.init_index()
    me.start()