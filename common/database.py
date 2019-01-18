#!/usr/bin/env python3
# encoding: utf-8

import redis
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from .utils import get_logger
from config import Config

class RedisClient:

    def __init__(
        self,db, host=Config.REDIS_HOST, port=Config.REDIS_PORT, password=Config.REDIS_PASSWORD
    ):
        conn_pool = redis.ConnectionPool(
            db=db,
            host=host,
            port=port,
            password=password,
            max_connections=Config.REDIS_MAX_CONNECTION,
        )
        self.redis = redis.Redis(connection_pool=conn_pool)
        self.logger = get_logger("logger_redis_{}".format(port))
        
    def add_magnet(self, magnet):
        """
        新增磁力链接
        """
        self.redis.sadd(Config.REDIS_KEY, magnet)

    def add_peer(self,infohash,address):
        """
        新增磁力peer信息
        """    
        self.redis.sadd('peer',str(infohash)+':'+address[0]+':'+str(address[1]))
        # if (self.redis.exists(infohash) == False):
        #     self.redis.sadd('peer',str(infohash)+':'+address[0]+':'+str(address[1]))
        # else:
        #     self.logger.info("该种子已存在:infohash>{0}".format(infohash))

    def set_keyinfo(self,infohash,metadata):
        """
        """    
        self.redis.set(infohash,metadata)
        print(str(infohash))


    def get_magnets(self, count=128):
        """
        返回指定数量的磁力链接
        """
        return self.redis.srandmember(Config.REDIS_KEY, count)

    def get_redis_byKey(self,key,count):
        """
        返回指定数量的磁力链接
        """
        return self.redis.srandmember(key, count)

    def getKeys(self):
        return self.redis.keys()

    def getValue(self,key):
        return self.redis.get(key)

    def deleteByKey(self,key):
        self.redis.delete(key)

RedisClients = RedisClient(0)
RedisClients1 = RedisClient(1)

class ElasticsClient:

    def __init__(self, index_name, index_type,
                    ip = Config.ELASTICS_HOST ,port = Config.ELASTICS_PORT, 
                    maxsize=Config.ELASTICS_MAX_CONNECTION):
        '''
        :param index_name: 索引名称
        :param index_type: 索引类型
        '''
        self.index_name =index_name
        self.index_type = index_type
        self.logger = get_logger("logger_elastics_")
        #用户名密码状态
        #self.es = Elasticsearch([ip],http_auth=('elastic', 'password'),port=9200)
        # 无用户名密码状态
        self.es = Elasticsearch([ip],port=port,maxsize=maxsize)

    def create_index(self,_index_mappings):
        '''
         param ex: Elasticsearch对象
        :return:
        '''
        if self.es.indices.exists(index=self.index_name) is not True:
            res = self.es.indices.create(index=self.index_name, body=_index_mappings)
            self.logger.info("创建索引索引成功 >>>> {0} - {1} !".format(self.index_name, self.index_type))
        # else:
        #     self.delete_index()
        #     self.create_index(_index_mappings)

    def delete_index(self):
        '''
        删除所有
        '''
        res = self.es.indices.delete(index=self.index_name)
        if(res['acknowledged']):
            self.logger.info("删除索引成功 >>>> {0} !".format(self.index_name))

    def Index_Data(self,list,infohash):
        '''
        数据存储到es
        :return:
        '''
        for item in list:
            res = self.es.index(index=self.index_name, doc_type=self.index_type, body=item, id=infohash)
            if(res['_shards']['successful'] == 1):
                self.logger.info("种子入库成功 >>>> {0} - {1}".format(infohash,res['_version']))
            

    def bulk_Index_Data(self):
        '''
        用bulk将批量数据存储到es
        :return:
        '''
        list = [
            {"date": "2017-09-13",
             "source": "慧聪网",
             "link": "http://info.broadcast.hc360.com/2017/09/130859749974.shtml",
             "keyword": "电视",
             "title": "付费 电视 行业面临的转型和挑战"
             },
            {"date": "2017-09-13",
             "source": "中国文明网",
             "link": "http://www.wenming.cn/xj_pd/yw/201709/t20170913_4421323.shtml",
             "keyword": "电视",
             "title": "电视 专题片《巡视利剑》广获好评：铁腕反腐凝聚党心民心"
             },
            {"date": "2017-09-13",
             "source": "人民电视",
             "link": "http://tv.people.com.cn/BIG5/n1/2017/0913/c67816-29533981.html",
             "keyword": "电视",
             "title": "中国第21批赴刚果（金）维和部隊启程--人民 电视 --人民网"
             },
            {"date": "2017-09-13",
             "source": "站长之家",
             "link": "http://www.chinaz.com/news/2017/0913/804263.shtml",
             "keyword": "电视",
             "title": "电视 盒子 哪个牌子好？ 吐血奉献三大选购秘笈"
             }
        ]
        ACTIONS = []
        i = 1
        for line in list:
            action = {
                "_index": self.index_name,
                "_type": self.index_type,
                "_id": i, #_id 也可以默认生成，不赋值
                "_source": {
                    "date": line['date'],
                    "source": line['source'].decode('utf8'),
                    "link": line['link'],
                    "keyword": line['keyword'].decode('utf8'),
                    "title": line['title'].decode('utf8')}
            }
            i += 1
            ACTIONS.append(action)
            # 批量处理
        success, _ = bulk(self.es, ACTIONS, index=self.index_name, raise_on_error=True)
        print('Performed %d actions' % success)

    def Delete_Index_Data(self,id):
        '''
        删除索引中的一条
        :param id:
        :return:
        '''
        res = self.es.delete(index=self.index_name, doc_type=self.index_type, id=id)
        print(res)

    def Get_Data_Id(self,id):

        res = self.es.get(index=self.index_name, doc_type=self.index_type,id=id)
        print(res['_source'])

        print('------------------------------------------------------------------')
        #
        # # 输出查询到的结果
        for hit in res['hits']['hits']:
            # print hit['_source']
            print(hit['_source']['date'],hit['_source']['source'],hit['_source']['link'],hit['_source']['keyword'],hit['_source']['title'])

    def Get_Data_By_Body(self,value):
        # doc = {'query': {'match_all': {}}}
        doc = {
                "query": {
                    "dis_max": {
                        "queries": [
                            { "match": { "bare_name": value }},
                            { "match": { "file_list": value }}
                        ],
                        "tie_breaker": 0.3
                    }
                }
            }
        
        _searched = self.es.search(index=self.index_name, doc_type=self.index_type, body=doc)
        return _searched['hits']['hits']
        # for hit in _searched['hits']['hits']:
        #      print(hit)
            #print(hit['_source']['date'], hit['_source']['source'], hit['_source']['link'], hit['_source']['keyword'],hit['_source']['title'])

