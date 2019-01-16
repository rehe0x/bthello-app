#!/usr/bin/env python3
# encoding: utf-8

from common.database import RedisClients,ElasticsClients

if __name__ == "__main__":
    #keys = RedisClients.getKeys()
    # for key in keys:
    #     print(key)

    # value = RedisClients.getValue('3bafba64d187893790bc3f406a3119b400046595')
    # v = eval(value)
    # print(v['bare_name'])

    ElasticsClients.Get_Data_By_Body()
    print(2)