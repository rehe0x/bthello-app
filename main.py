#!/usr/bin/env python3
# encoding: utf-8

from common.database import RedisClients
from metadata_storage import MetadataStorage

if __name__ == "__main__":
    #keys = RedisClients.getKeys()
    # for key in keys:
    #     print(key)

    # value = RedisClients.getValue('3bafba64d187893790bc3f406a3119b400046595')
    # v = eval(value)
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
   
    #ElasticsClients.Get_Data_By_Body()
    # ElasticsClients.delete_index('test')
    # print(2)
    me = MetadataStorage()
    me.start()